from firebase import firebase
firebaseadmin = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)
data = {'nameadmin': 'admin',
        'paswordadmin': 'admin'
        }

allusers = firebaseadmin.get('/Admin',None)
print(allusers)

#pip install git+https://github.com/ozgur/python-firebase

