class student:
    sname:str
    sid:int
    age:int
    gender:str
    course:str
    contact:int
    address:str


    def __init__(self,name,id,age,gender,course,contact,address):
        self.sname=name
        self.sid=id
        self.age=age
        self.gender=gender
        self.course=course
        self.contact=contact
        self.address=address

    def display_student(self):
        print(self.sname,self.sid,self.age,self.gender,self.course,self.contact,self.address)

student_instance=student("pranav",100,20,"male","python",345678934567,"address")
 
student_instance.display_student()