from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
import os
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

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'},

app = Flask(__name__)
app.config.update(
    UPLOAD_FOLDER = 'static/temp',
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'},
    TESTING = True,
)

@app.route("/")
def home():
    if session.get('logged_in'):
        return render_template("index.html")
    else:
        lastuser = session.get('lastuser')
        message = session.get('message')
        return redirect("login.html", lastuser=lastuser, message=message)

@app.route

def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
        
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
                session['lastuser'] = userAccounts[esername]['firstname']
                print(f"username: {esername} with pass: {eserpass} LOGIN SUCCESS")
                return home()

            else: 
                error = 'Incorrect Password'
                print(f"username: {esername} with pass: {eserpass} INCORRECT PASSWORD")
                return render_template("login.html", error=error)

        else:
            error = 'User does not exist'
            print(f"username: {esername} with pass: {eserpass} USER DOES NOT EXIST!")
            return render_template("login.html", error=error)

    return render_template("login.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
                    image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image.thumbnail((320,320))
                    image.save('static/userpictures/{filename}')
                else:
                    message_minor = "Invalid profile picture was uploaded"
        else:
            message_minor = "Make sure to setup your profile picture sometime!"


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
                    }
                })
                message = "You're now registered, please login using your details"
                return render_template("login.html",message=message,message_minor=message_minor)
            else:
                error = "Passwords don't match, please repeat your password again"
        else:
            error = "User is already registered, please log in instead"
            return render_template("register.html", error=error)

    return render_template("register.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['message'] = 'Thank you for visiting our shop!'
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)