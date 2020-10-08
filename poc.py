from firebase import firebase
firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
data = {'_name':'unique22',
        'nameadmin': 'admin122',
        'paswordadmin': 'admin122'
        }

searched_user = firebaseuser.get('/Admin', name='aa')

print(searched_user)
#firebaseuser.put('/Admin',data=data,name='new1')
#
#
searched_user = firebaseuser.get('/Admin', None)
print(searched_user)
#
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
#
# a = [10,20,30,20,10,50,60,40,80,50,40]
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = li1.copy()
# print("Original List:", li1)
# print("After Cloning:", li2)
