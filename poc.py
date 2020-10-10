from firebase import firebase
firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)

searched_user = firebaseuser.get('/Admin', name='aa')

print(searched_user)
data={'Compaint_type':'leeeeeee'}
firebaseuser.put('/Admin/144/Complaint/1',data=data,name='new1')
#
#
searched_user = firebaseuser.get('/Admin', name='new1')
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
