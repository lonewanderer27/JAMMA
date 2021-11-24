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
userAccounts = {
'Adriane': {
    'firstname': 'Adriane', 
    'lastname': 'Puzon', 
    'username': 'Adriane', 
    'userpass': 'k0yk0y@503_JAMMA', 
    'usertel': '+639983082814'}, 
    
'JOY': {
    'username': 'JOY', 
    'userpass': 'k0yk0y@503_JOMMA', 
    'userprofile': 'Noneyet'}, 

'Joy': {
    'username': 'Joy', 
    'userpass': 'k0yk0y@503_JOMMA', 
    'userprofile': 'Noneyet'}, 

'aziaziazi': {
    'firstname': 'Winston Earl', 
    'lastname': 'Puzon', 
    'username': 'aziaziazi', 
    'userpass': 'k0yk0y@503_JAMMA3', 
    'usertel': ''}, 
    
'fredpuzon74': {
    'firstname': 'Fred', 
    'lastname': 'Puzon', 
    'username': 'fredpuzon74', 
    'userpass': 'k0yk0y@503_JAMMA2', 
    'usertel': ''}, 

'keitarojay27': {
    'firstname': 'Keitaro Jay', 
    'lastname': 'Puzon', 
    'username': 'keitarojay27', 
    'userpass': 'k0yk0y@503_JAMMA2', 
    'usertel': ''}
}

esername = 'Adriane'
eserpass = 'k0yk0y@503_JAMMA'

if esername in userAccounts:
    print(userAccounts[esername]["username"])
    print(userAccounts[esername]["userpass"])

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

# image = Image.open('static/temp_userprofiles/PUZON.jpg')
# # image.show()
# image.thumbnail((320,320))
# image.save('static/userprofiles/PUZON.jpg')

# image = Image.open('static/userprofiles/PUZON.jpg')
# image.show()

