from firebase import firebase
firebase = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/UserRegister/', None)
data = {'Name': 'test',
        'RollNo': 3,
        'Percentage': 70.02
        }
result = firebase.post('/UserRegister', data)
print(result)
pip install git+https://github.com/ozgur/python-firebase