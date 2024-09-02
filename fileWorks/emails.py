email_ids=[
    "sam@gmail.com",
    "smith@gmail.com",
    "jhon@gmail.com",
    "stuart@gmail.com",
    "james@gmail.com",
]

emails=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\emails.txt","w")
for email in email_ids:
    emails.write(email+"\n") 