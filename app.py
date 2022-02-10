from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
from flask_talisman import Talisman
import os, time
import firebase_admin
from firebase_admin import credentials, db, storage
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime
import logging
from operator import itemgetter  


# Fetch the service account key JSON file contents
cred = credentials.Certificate('jamma-firebase-adminsdk-credentials.json')

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

#for load testing purposes
@app.route("/loaderio-8f82c94de57fbc8606728068c3bba183/", methods=['GET'])
def loaderio():
    return "loaderio-8f82c94de57fbc8606728068c3bba183"




@app.route("/", methods=['GET'])
def home():
    if session.get('logged_in'):
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        jammaLink = "https://jammacomments.herokuapp.com?"+"username="+username+"&profile_url="+profile_url
        active_category = 'featured'
        print(jammaLink)
        return render_template(
            "index.html", 
            jammaLink=jammaLink, 
            username=username, 
            profile_url=profile_url, 
            active_category=active_category)
    else:
        return redirect(url_for('login'))



@app.route("/index", methods=['GET'])
def index():
    if session.get('logged_in'):
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        usermail = session.get('usermail')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        active_category = 'featured'

        ref = db.reference('/products')
        new_products = ref.order_by_key().limit_to_last(5).get()
        products = ref.get()

        ref = db.reference('productsSales')
        productsSales = ref.get()
        sorted_productsSales = {}
        counter = 0
        for key, value in sorted(productsSales.items(), key = itemgetter(1), reverse = True):
            counter += 1
            if counter < 6:
                sorted_productsSales[key] = value
        
        return render_template(
            "index.html", 
        jammaLink=jammaLink, 
        username=username, 
        profile_url=profile_url, 
        usermail=usermail,
        active_category=active_category,
        new_products=new_products,
        products=products,
        sorted_productsSales=sorted_productsSales,
        )
        
    else:
        return redirect(url_for('login'))



@app.route("/allproducts", methods=['GET', 'POST'])
def allproducts():
    if session.get('logged_in'):
        if request.method == "POST":
            pass
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        usermail = session.get('usermail')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        active_category = 'allproducts'
        ref = db.reference('/products')
        products = ref.get()
        return render_template(
            "allproducts.html", 
            jammaLink=jammaLink, 
            username=username, 
            usermail=usermail,
            profile_url=profile_url, 
            active_category=active_category,
            products=products,
            )

    else:
        return redirect(url_for('login'))
    


@app.route("/smartwatch", methods=['GET', 'POST'])
def smartwatch():
    if session.get('logged_in'):
        if request.method == "POST":
            pass
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        usermail = session.get('usermail')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        active_category = 'smartwatch'
        ref = db.reference('/products')
        products = ref.get()

        #Removes non-earphone products in products dictionary
        products = filterproducts(products, 'smartwatch')

        return render_template(
            "smartwatch.html", 
            jammaLink=jammaLink, 
            username=username, 
            usermail=usermail,
            profile_url=profile_url, 
            active_category=active_category,
            products=products,
            )

    else:
        return redirect(url_for('login'))




def filterproducts(products, category):
    products_temp = {}
    for product in products:
        if products[product]['productCategory'] == category:
            products_temp[product] = products[product]
    products = products_temp
    return products
        



@app.route("/earphone", methods=['GET', 'POST'])
def earphone():
    if session.get('logged_in'):
        if request.method == "POST":
            pass
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        usermail = session.get('usermail')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        active_category = 'earphone'
        ref = db.reference('/products')
        products = ref.get()

        #Removes non-earphone products in products dictionary, that is going to be passed to the html template
        products = filterproducts(products, 'earphone')

        return render_template(
            "earphone.html", 
            jammaLink=jammaLink, 
            username=username, 
            usermail=usermail,
            profile_url=profile_url, 
            active_category=active_category,
            products=products,
            )

    else:
        return redirect(url_for('login'))



@app.route("/about", methods=['GET', 'POST'])
def about():
    if session.get('logged_in'):
        if request.method == "POST":
            pass
        username = session.get('lastuser')
        profile_url = session.get('profile_url')
        usermail = session.get('usermail')
        jammaLink = "https://jammacomments.herokuapp.com/?"+"username="+username+"&profile_url="+profile_url
        active_category = 'about'
        return render_template(
            "about.html", 
            jammaLink=jammaLink, 
            username=username,
            usermail=usermail,
            profile_url=profile_url, 
            active_category=active_category)

    else:
        return redirect(url_for('login'))



@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        lastuser = session.get('lastuser')
        message = session.get('message')
        message_minor = session.get('message_minor')
        if request.method == "POST":
            esername = request.form['username']
            eserpass = request.form['userpass']
            ref = db.reference('/userAccounts')
            userAccounts = ref.get()
            if esername in userAccounts:
                if userAccounts[esername]["userpass"] == eserpass:
                    session['logged_in'] = True
                    session['lastuser'] = userAccounts[esername]['username']
                    session['profile_url'] = userAccounts[esername]['profile_url']
                    session['usermail'] = userAccounts[esername]['usermail']

                    visitor_ip_address = request.remote_addr
                    logging.info(f"LOGIN SUCCESS    username: {esername}   password: {eserpass}    IP Address: {visitor_ip_address}")

                    return redirect(url_for('index'))

                else: 
                    error = 'Incorrect Password'
                    logging.warning(f"INCORRECT PASSWORD    username: {esername}   password: {eserpass}")
                    return render_template("login.html", error=error)

            else:
                error = 'User does not exist'
                logging.warning(f"USER DOES NOT EXIST    username: {esername}   password: {eserpass}")
                return render_template("login.html", error=error)

        return render_template(
            "login.html", lastuser=lastuser, message=message, message_minor=message_minor)
        



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route("/preregister")
def preregister():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        session['error'] = None
        return redirect(url_for('register'))



def empty_profile_url():
    bucket = storage.bucket()
    blob = bucket.blob("userpictures/Default_Profile.png")
    blob.make_public()
    profile_url = (blob.public_url)
    return profile_url



def currentDateTime():
    now = datetime.now()
    datetime_complete_string = now.strftime("%d/%m/%Y %H:%M:%S:%f")
    return datetime_complete_string



@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
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
                    logging.info(f"{esername} successfully uploaded a profile picture")



                else:
                    session['message_minor'] = "Invalid profile picture was uploaded"
                    profile_url = empty_profile_url()
                    logging.warning(f"{esername} uploaded an invalid picture")

            else:
                session['message_minor'] = "Make sure to setup your profile picture sometime!"
                profile_url = empty_profile_url()
                print(f"{esername} did not upload any photo")
                logging.warning(f"{esername} did not uploaded any photo")


            print("profile_url : "+profile_url)


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
                            'registerDate&Time': currentDateTime(),
                            'ip': request.remote_addr
                        }
                    })
                    session['message'] = "You're now registered " +esername+ " please login"
                    visitor_ip_address = request.remote_addr
                    logging.info(f"REGISTRATION SUCCESS    username: {esername}   password: {eserpass}    IP Address: {visitor_ip_address}")
                    return redirect(url_for('index'))

                else:
                    error = "Passwords don't match, please repeat your password again"
                    return render_template("register.html", error=error)
                    
            else:
                error = "Username " + esername + " is already taken"
                return render_template("register.html", error=error)

        return render_template("register.html")



@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['message'] = None
    return redirect(url_for('index'))



@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404


# Wrap Flask app with Talisman
Talisman(app, force_https_permanent=True, content_security_policy=None)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)