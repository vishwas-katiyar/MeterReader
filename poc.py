# from firebase import firebase
# firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/', None)
# allusers=searched_user = firebaseuser.get('/UserRegister', '')
# verified_user=0
# not_verified_user=0
# user_complaint=0
# total_user=len(allusers)
# Complaints=0
# Appli_suggetion=0
# Emergency_Complaints=0
# reply=0
# for i in allusers:
#     if allusers[i]['auth']=='true':
#         verified_user += 1
#     else:
#         not_verified_user += 1
#     if 'Complaints' in allusers[i].keys():
#         user_complaint+=1
#         for j in allusers[i]['Complaints']:
#             if j :
#                 if j['complaintType']=='Emergency Complaints':
#                     Emergency_Complaints+=1
#                 elif j['complaintType']=='Application/Suggestions':
#                     Appli_suggetion+=1
#                 else:
#                     Complaints+=1
#                 if 'reply' in j.keys():
#                     reply+=1
#     print(allusers[i])
#
# def v():
#     return print('vvvv')
# def v():
#     return print('ppppv')
# v()



#
# camera = image
# qr=image    qrcoadreader
# qrcoadreader=qr
# crop=camera
# txtetract=crop
# import qrcode
# img = qrcode.make(1234)
# img.save('imagename.jpg')

# searched_user = firebaseuser.get('/UserRegister',name='0130')
# print(searched_user)
# count=-1
# for i in searched_user['Complaints']:
#     count+=1
#     if i:
#         if i['complaintMessage']=='this is suggestion':
#             print(i)
#             firebaseuser.put('/UserRegister/' + '0130' + '/Complaints/' + str(count) + '/',
#                              'reply', 'myyyyyy')

# print(searched_user['auth'])
# # a=[]
#
# for i in searched_user['MeterReading']:
#     print(i)
#     a.append(list(searched_user['MeterReading'][i].keys())[0])
#     a.append(list(searched_user['MeterReading'][i].values())[0])
# print(a)

# firebaseuser.put('/UserRegister/1628/Complaints/'+str(1),'reply','this is reply')
# searched_user = firebaseuser.get('/UserRegister',name=1628)
# print(searched_user)
#
# print(searched_user)
# complaint=[]
# emergency_ivrs=[]
# emergency_dict={}
# emergency_ivrs_complaint=[]
# complaint_ivrs=[]
# complaint_dict={}
# complaint_ivrs_complaint=[]
# appli_sugg_ivrs=[]
# appli_sugg_dict= {}
# appli_sugg_ivrs_complaint=[]
# for i in searched_user:
#     #print(i)
#
#     if 'Complaints' in searched_user[i].keys():
#         complaint.append(i)
#         for j in searched_user[i]["Complaints"][1:]:
#             val=j.values()
#             if 'Emergency Complaints' in val:
#                 emergency_ivrs.append(i)
#                 emergency_ivrs_complaint.append(j['complaintMessage'])
#                 if i in emergency_dict.keys():
#                     emergency_dict[i]=[emergency_dict[i],j['complaintMessage']]
#                 else:
#                     emergency_dict[i]=[j['complaintMessage']]
#             elif 'Complaints' in val:
#                 complaint_ivrs.append(i)
#                 complaint_ivrs_complaint.append(j['complaintMessage'])
#                 if i in complaint_dict.keys():
#                     print(complaint_dict[i])
#                     print(str(j['complaintMessage']))
#                     complaint_dict[i]=complaint_dict[i]+[j['complaintMessage']]
#                 else:
#                     complaint_dict[i]=[j['complaintMessage']]
#             elif 'Application/Suggestions' in val:
#                 appli_sugg_ivrs.append(i)
#                 appli_sugg_ivrs_complaint.append(j['complaintMessage'])
#                 if i in appli_sugg_dict.keys():
#                     appli_sugg_dict[i]=appli_sugg_dict[i].insert(j['complaintMessage'])
#                 else:
#                     appli_sugg_dict[i]= [j['complaintMessage']]
#  #       print(searched_user[i]["Complaints"][1:])
#
# #print(complaint)
# print(appli_sugg_ivrs)
# print(appli_sugg_ivrs_complaint)
# print(appli_sugg_dict)
# print(emergency_ivrs)
# print(emergency_ivrs_complaint)
# print(emergency_dict)
# print(list(set(complaint_ivrs)))
# print(complaint_ivrs_complaint)
# print(complaint_dict)
#
#
#
# x=['a']
# y='b'
# p=x+[y]
# print(p)
#
# # firebaseuser.put('/UserRegister/'+str(444)+'/MeterReading/44400102020','12_12_2020','00' )
# searched_user = firebaseuser.get('/UserRegister', name='444')
# print(searched_user)
# # print(searched_user['Complaints'][1])
# # #/
# from datetime import date
#
# today = date.today()
# _today=str(date.today()).replace('-','/')
# print(_today)
# print(today.year)
# print(today.month)
# print(today)

# firebaseuser.put('/UserRegister/' + str(123)+'/MeterReading', str(123)+'0010201/link/', 'hiiii11')
#
from docxtpl import DocxTemplate
# # # import json
# # # #
# firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/', None)
# # #
# # #
doc = DocxTemplate("MeterReaderApp/Static/SampleBill.docx")
# #
context_doc = {'meterNumber': '123456789',
                    'customer_name': 'avsss',
                    'previousYear': 123,
                    'currentYear': 123
                    }
doc.render(context_doc)
doc.save("MeterReaderApp/Static/GeneratedBill.pdf")
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

# #
# import requests
# url = 'http://mymeterreader.herokuapp.com/test'
# myobj = {'ivrs': '0130',
#          'CurrentDate':'2020_11_06',
#          'CurrentReading':65,
#          }
# x = requests.post(url, data = myobj)
# # print(x.status_code, x.qreason)
# print('jhgkjhghgjk',x.text)
# # #

#
#
# def login():
#     h=1
#
#
#
# def loginh():
#     if h:
#













# Define a blank dictionary with no elements
#
# initial=int(input("Enter initial range :"))
# final=int(input("Enter final range :"))
# n=int(input("Enter the number to divided by :"))
# a=[]
# for i in range(initial,final+1):
#     if(i%n == 0):
#         a.append(i)
# print('Number  {0}  can divided in range from {1} to {2}  is {3}'.format(n,initial,final,a))
#
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


# s={}
# s['1']=['one']
# print(s)
# print(s['1'])
# s['1'].append('two')
# print(s)
#



#
#
# a = [10,20,30,20,10,50,60,40,80,50,40]
#
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = li1.copy()
# print("Original List:", li1)
# print("After Cloning:", li2)
#
# #
# user = firebaseuser.get('/UserRegister', name='444')
# print(user['auth'])
# for i in user:
#     print(i)
#
#
#




#
# #
# a=user['MeterReading'][list(user['MeterReading'].keys())[-2]]
# print(list(a.keys())[0].replace('_',','))
# # print(list(a.values())[0])
# c='12,12,2016'
# d='12,3,2016'
#
# from datetime import datetime
# date_format = "%d,%m,%Y"
# a = datetime.strptime(c, date_format)
# b = datetime.strptime(d, date_format)
# delta = b - a
# # #print delta.days # that's it
# # print(delta.days)
# if c[3:5] == 12:
#     c[3:5]='01'
# else :
#     c[3:5]=str(int(c[3:5])+1)
# print(c)
#
# s="2020-01-28"
# y=s[:4]
# m=s[5:7]
# d=s[8:]
#
# print(y,m,d)