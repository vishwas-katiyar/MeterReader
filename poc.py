# # from firebase import firebase
# from docxtpl import DocxTemplate
# # import json
# #
# # firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
# #
# #
# doc = DocxTemplate("MeterReaderApp/Static/SampleBill.docx")
# #
# context_doc = {'meterNumber': '123456789',
#                     'customer_name': 'avsss',
#                     'previousYear': 123,
#                     'currentYear': 123
#                     }
# doc.render(context_doc)
# doc.save("MeterReaderApp/Static/generated/GeneratedBill.docx")
# # q=doc.toJSON()
#
# firebaseuser.put('/Admin', data={'abcd':q}, name='new1')
# ##
# #
# searched_user = firebaseuser.get('/Admin', name='new1')
# print(searched_user)
# #
# '''
# requestlist=[]
# for i in allusers:
#         if allusers[i]['auth']:
#                 print(allusers[i]['auth'])
#                 requestlist.append(allusers[i])
# print(requestlist)
# #pip install git+https://github.com/ozgur/python-firebase
#
# #chmod +x MeterReaderApp/Tesseract-OCR/tesseract.exe
# '''
#

import requests
url = 'http://mymeterreader.herokuapp.com/test/'
myobj = {'hii': 'somevalue111'}
x = requests.post(url, data = myobj)
# print(x.status_code, x.reason)
# print(x.text)
import json



print(x)




# # print(x)
# from firebase_admin import credentials, initialize_app, storage
# # Init firebase with your credentials
# cred = credentials.Certificate("login-system-73453-5ca66a2acaee.json")
# initialize_app(cred, {'storageBucket': 'login-system-73453.appspot.com'})
#
# # Put your local file path
# fileName = "MeterReaderApp/Static/generated/GeneratedBill.docx"
# bucket = storage.bucket()
# blob = bucket.blob(fileName)
# blob.upload_from_filename(fileName)
#
# # Opt : if you want to make public access from the URL
# blob.make_public()
#
# print("your file url", blob.public_url)



#
#
# a = [10,20,30,20,10,50,60,40,80,50,40]
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = li1.copy()
# print("Original List:", li1)
# print("After Cloning:", li2)
