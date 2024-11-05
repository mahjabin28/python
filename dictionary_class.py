student={'id1':
    {'Name':'Sarah',
    'Class':'2',
    'Subject':['math','English'],
    },
    'id2':
    {'Name':'Rifa',
     'Class':'2',
     'Subject':['Math','science']

    },
    'id3':
    {'Name':'Rifa',
     'Class':'2',
     'Subject':['Math','science']

    }}
result={}
for key,value in student.items():
    if value not in result.values():
        result[key]=value

print(result)

         
         