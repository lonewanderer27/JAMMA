# from flask import Flask
# from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import firebase_admin
from firebase_admin import credentials, db, storage
import passchecker
from PIL import Image

# Fetch the service account key JSON file contents
cred = credentials.Certificate('jamma-comments-332612-firebase-adminsdk-9x87k-8d8cbd899a.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jamma-comments-332612-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'jamma-comments-332612.appspot.com'
})



# # As an admin, the app has access to read and write all data, regradless of Security Rules
# username = 'Adriane'
# userpass = 'k0yk0y@503_JAMMA'
# userprofile = 'Noneyet'


# ref = db.reference('/userAccounts')
# ref.update({
#     username: {
#         'username': username,
#         'userpass': userpass,
#         'userprofile': userprofile,
#     }
# })

# username = 'JOY'
# userpass = 'k0yk0y@503_JOMMA'
# userprofile = 'Noneyet'


# ref = db.reference('/userAccounts')
# ref.update({
#     username: {
#         'username': username,
#         'userpass': userpass,
#         'userprofile': userprofile,
#     }
# })

# username = 'Joy'
# userpass = 'k0yk0y@503_JOMMA'
# userprofile = 'Noneyet'


# ref = db.reference('/userAccounts')
# ref.update({
#     username: {
#         'username': username,
#         'userpass': userpass,
#         'userprofile': userprofile,
#     }
# })


# userAccounts = {
# 'Adriane': {
#     'firstname': 'Adriane', 
#     'lastname': 'Puzon', 
#     'username': 'Adriane', 
#     'userpass': 'k0yk0y@503_JAMMA', 
#     'usertel': '+639983082814'}, 
    
# 'JOY': {
#     'username': 'JOY', 
#     'userpass': 'k0yk0y@503_JOMMA', 
#     'userprofile': 'Noneyet'}, 

# 'Joy': {
#     'username': 'Joy', 
#     'userpass': 'k0yk0y@503_JOMMA', 
#     'userprofile': 'Noneyet'}, 

# 'aziaziazi': {
#     'firstname': 'Winston Earl', 
#     'lastname': 'Puzon', 
#     'username': 'aziaziazi', 
#     'userpass': 'k0yk0y@503_JAMMA3', 
#     'usertel': ''}, 
    
# 'fredpuzon74': {
#     'firstname': 'Fred', 
#     'lastname': 'Puzon', 
#     'username': 'fredpuzon74', 
#     'userpass': 'k0yk0y@503_JAMMA2', 
#     'usertel': ''}, 

# 'keitarojay27': {
#     'firstname': 'Keitaro Jay', 
#     'lastname': 'Puzon', 
#     'username': 'keitarojay27', 
#     'userpass': 'k0yk0y@503_JAMMA2', 
#     'usertel': ''}
# }

# esername = 'Adriane'
# eserpass = 'k0yk0y@503_JAMMA'

# if esername in userAccounts:
#     print(userAccounts[esername]["username"])
#     print(userAccounts[esername]["userpass"])

# eserpass = 'k0yk0y@503_JAMMA'
# esername = 'Adriane'

# bucket = storage.bucket()
# ref = db.reference('/userAccounts/')    #assigns reference as userAccounts
# userAccounts = ref.get()    #retrieves and gets the rerefenced part from Firebase
# print(userAccounts)
# if esername in userAccounts:
#     print(esername['userpass'])

    # if (passchecker.ob.strongPasswordChecker(eserpass) > 0):
    #     print("Weak password")
    # else:
    #     print("Strong password")
# import os

# filename = 'PUZON.jpg'
# image = Image.open('static/temp/PUZON.jpg')
# # image.show()
# image.thumbnail((320,320))
# image.save(os.path.join("static/temp",filename))

# filename = 'PUZON.jpg'
# image = Image.open(os.path.join("static/userpictures",filename))
# image.show()

# filename = 'userpictures/Adriane.png'
# file = 'static/userpictures/Adriane.png'
# format = "image/png"

# bucket = storage.bucket()
# blob = bucket.blob(filename)
# blob.upload_from_filename(file,content_type=format)

messages = {
    "-Mp28J7ILF9hDw4XWH_8" : {
        "body" : "eyyy eyyy eeeeeeeeeeeeeeeeeey ",
        "deleted" : "True",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 23:37:34",
        "userEmail" : "",
        "userName" : "jay",
        "userTel" : ""
    },
    "-Mp29Qz70apyiMebtnd8" : {
        "body" : "This is going to be the final test! ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 23:42:28",
        "userEmail" : "",
        "userName" : "jay",
        "userTel" : ""
    },
    "-Mp29YgkbCNwJSJ-n5fk" : {
        "body" : "Subarashi sugoi oniichaaaaaaaan ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 23:43:00",
        "userEmail" : "",
        "userName" : "Niko Niko Nikoniiiiiii",
        "userTel" : ""
    },
    "-Mp29fiqOHoDiSWY_tEw" : {
        "body" : "LOL! **** YOU! ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 23:43:33",
        "userEmail" : "",
        "userName" : "tessssstingggg againnn!!",
        "userTel" : ""
    },
    "-Mp29msoKFfaw6HBDzN8" : {
        "body" : "Wow ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 15:44:02",
        "userEmail" : "",
        "userName" : "Sir",
        "userTel" : ""
    },
    "-Mp2A-Wfk2Fgx6Sc1Ufa" : {
        "body" : "**** **** this **** website ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Default_Profile.png",
        "timestamp" : "2021-11-21 15:44:58",
        "userEmail" : "",
        "userName" : "Seil Wiper",
        "userTel" : ""
    },
    "-MpKm26SkLaT8x3JOL2_" : {
        "body" : "THE PROFILE PICTURE FINALLY WORKS! ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Adriane.png",
        "timestamp" : "2021-11-25T06:28:42.511088",
        "userName" : "Adriane"
    },
    "-MpL-D6Xx10sqvL4S8TE" : {
        "body" : "Testing if the profile picture works",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Adriane.png",
        "timestamp" : "2021-11-25T07:30:37.609412",
        "userName" : "Adriane"
    },
    "-MpMV6363roYFtDiFvYB" : {
        "body" : "THE COMMENT SECTION IS NOW WORKING PROPERLY OMG! ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/Adriane.png",
        "timestamp" : "2021-11-25T14:29:34.514201",
        "userName" : "Adriane"
    },
    "-MpMY4TDKH1XOQmn0Ly0" : {
        "body" : "New feature: When logged in with JAMMA, you don't have to log in separately in JAMMA Comments, it automatically logs you in so you can participate right away! ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/boombox.png",
        "timestamp" : "2021-11-25T14:42:34.396235",
        "userName" : "boombox"
    },
    "-MpMYFeSo7VxsQM5yFWj" : {
        "body" : "And oh! Haven't I mentioned that your comment appears right away after you submitted it? Pretty amazing huh? ",
        "profile_url" : "https://storage.googleapis.com/jamma-comments-332612.appspot.com/userpictures/boombox.png",
        "timestamp" : "2021-11-25T14:43:20.263429",
        "userName" : "boombox"
    }
}


