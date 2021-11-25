from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
import os, time
import firebase_admin
from firebase_admin import credentials, db, storage
from PIL import Image
from werkzeug.utils import secure_filename

# Fetch the service account key JSON file contents
cred = credentials.Certificate('jamma-comments-332612-firebase-adminsdk-9x87k-8d8cbd899a.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jamma-comments-332612-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'jamma-comments-332612.appspot.com'
})

app = Flask(__name__)
app.config.update(
    UPLOAD_FOLDER = 'static/temp',
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'},
    TESTING = True,
)

@app.route("/", methods=['GET'])
def home():
    if session.get('logged_in'):
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        jammaLink = "https://jammacomments.herokuapp.com?"+"username="+username+"&profile_url="+profile_url
        print(jammaLink)
        return render_template("index.html", jammaLink=jammaLink)
    else:
        lastuser = session.get('lastuser')
        message = session.get('message')

        return render_template("login.html", lastuser=lastuser, message=message)

@app.route("/index", methods=['GET'])
def index():
    if session.get('logged_in'):
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        print(jammaLink)
        return render_template("index.html", jammaLink=jammaLink)
    else:
        lastuser = session.get('lastuser')
        message = session.get('message')

        return render_template("login.html", lastuser=lastuser, message=message)




@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        esername = request.form['username']
        eserpass = request.form['userpass']
        ref = db.reference('/userAccounts')
        userAccounts = ref.get()
        if esername in userAccounts:
            if userAccounts[esername]["userpass"] == eserpass:
                session['logged_in'] = True
                session['lastuser'] = userAccounts[esername]['username']

                session['profile_url'] = userAccounts[esername]["profile_url"]
                print(f"username: '{esername}' with pass: '{eserpass}'\nLOGIN SUCCESS")
                return home()

            else: 
                error = 'Incorrect Password'
                print(f"username: '{esername}' with pass: '{eserpass}'\nINCORRECT PASSWORD")
                return render_template("login.html", error=error)

        else:
            error = 'User does not exist'
            print(f"username: '{esername}' with pass: '{eserpass}'\nUSER DOES NOT EXIST!")
            return render_template("login.html", error=error)

    return render_template("login.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route("/preregister")
def preregister():
    session['error'] = None
    return redirect(url_for('register'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        eserfname = request.form['fname']
        eserlname = request.form['lname']
        esername = request.form['username']
        esermail = request.form['usermail']
        eserpass = request.form['userpass']
        eserpass2 = request.form['userpass2']
        esertel = request.form['usertel']


        if 'userpicture' in request.files:
            eserpicture = request.files['userpicture']
            if eserpicture.filename != "":
                if eserpicture and allowed_file(eserpicture.filename):
                    filename = secure_filename(eserpicture.filename)
                    eserpicture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 

                    split_filename = filename.split(".")
                    split_filename[0] = esername
                    split_filename[1] = 'png'
                    newfilename = ('.'.join(split_filename))


                    image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image.thumbnail((320,320))
                    image.save(os.path.join("static/userpictures",newfilename))

                    bucket = storage.bucket()
                    blob = bucket.blob(os.path.join("userpictures/",newfilename))
                    blob.upload_from_filename(os.path.join("static/userpictures",newfilename),content_type="image/png")
                    blob.make_public()
                    profile_url = (blob.public_url)

                else:
                    session['message_minor'] = "Invalid profile picture was uploaded"
        else:
            session['message_minor'] = "Make sure to setup your profile picture sometime!"


        if request.form.get('profile_url') == None:
            bucket = storage.bucket()
            blob = bucket.blob("userpictures/Default_Profile.png")
            blob.make_public()
            profile_url = (blob.public_url) 


        ref = db.reference('/userAccounts')
        userAccounts = ref.get()
        if esername not in userAccounts:
            if eserpass == eserpass2:
                ref.update({
                    esername: {
                        'firstname': eserfname,
                        'lastname': eserlname,
                        'usermail': esermail,
                        'usertel': esertel,
                        'username': esername,
                        'userpass': eserpass,
                        'profile_url': profile_url,
                    }
                })
                session['message'] = "You're now registered " +esername+ " please login"
                return redirect(url_for('index'))
            else:
                error = "Passwords don't match, please repeat your password again"
        else:
            error = "Username " + esername + " is already taken"
            return render_template("register.html", error=error)

    return render_template("register.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['message'] = 'Thank you for visiting our shop!'
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)