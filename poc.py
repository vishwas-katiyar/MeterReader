# from firebase import firebase
# firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
#
# searched_user = firebaseuser.get('/Admin', name='aa')
# firebaseuser.put('/Admin', data={'abcd':'as'}, name='new1')
##
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


import requests

url = 'https://mymeterreader.herokuapp.com/test/'
myobj = {'hii': 'somevalue'}
x = requests.post(url, data = myobj)
print(x.status_code, x.reason)
print(x.text)










#
#
# a = [10,20,30,20,10,50,60,40,80,50,40]
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = li1.copy()
# print("Original List:", li1)
# print("After Cloning:", li2)
