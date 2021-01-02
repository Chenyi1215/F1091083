class Student:
    def __init__(self,std_num,username,password,enter_year,gender,birth):
        self.std_num = std_num
        self.username = username
        self.password = password
        self.enter_year = enter_year
        self.gender = gender
        self.birth = birth
        self.classname = []


class Professor:
    def __init__(self,pid,username,password,gender,birth):
        self.pid = pid
        self.username = username
        self.password = password
        
        self.gender = gender
        self.birth = birth
        

class Manager:
    def __init__(self,username,password):
        self.username = username
        self.password = password


class Class:
    def __init__(self,num,classname,points,professor,tp):
        self.num = num
        self.classname = classname
        self.points = points
        self.professor = professor
        self.tp = tp