from firebase import firebase
firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
data = {'_name':'unique',
        'nameadmin': 'admin1',
        'paswordadmin': 'admin1'
        }

searched_user = firebaseuser.get('/UserRegister', name='144')

print(searched_user)
firebaseuser.put('/UserRegister/144','name1','11chiku..','144',144 )


searched_user = firebaseuser.get('/UserRegister', name='144')
print(searched_user)

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