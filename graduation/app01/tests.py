from django.test import TestCase

# Create your tests here.


import pyodbc

connection = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};SERVER=DESKTOP-V7UFE9Q;DATABASE=TeachingResearchV2;UID=hengliy;PWD=123456789')
curs = connection.execute('select * from tblUserInfo')
a=curs.fetchone()
print(a)
