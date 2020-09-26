from firebase import firebase
firebaseadmin = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
data = {'_name':'unique',
        'nameadmin': 'admin1',
        'paswordadmin': 'admin1'
        }
allusers = firebaseadmin.get('/UserRegister',None)
#firebaseadmin.put('/Admin',name='miii',data=data)
print(allusers)

for i ,j in allusers.items():
        print(i)
        print(j)

'''
requestlist=[]
for i in allusers:
        if allusers[i]['auth']:
                print(allusers[i]['auth'])
                requestlist.append(allusers[i])
print(requestlist)
#pip install git+https://github.com/ozgur/python-firebase

#chmod +x MeterReaderApp/Tesseract-OCR/tesseract.exe
'''