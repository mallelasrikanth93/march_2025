# class cname():
#     attr
#     methods

# class details(): #class definition
#     user_name = "harika" #attributes
#     id = 1234   #attributes
#     def user_info(self):#method defintion
#         print(f"username is {self.user_name} and id is {self.id}")
#     def user_info_2(self):
#         print("this is second info method")
#         self.user_info()
#         print(self.user_name,self.id)
# #Syntax
# #objname = classname()
# obj = details()
# # print(obj.user_name)
# # print(obj.id)
# # obj.user_info()
# obj.user_info_2()

# class mobile_phone():#class definition
#     bn = "samsung" #attributes
#     color = "white" #attr
#     storage = "128gb"#attr
#     def calling(self,mobile_name):
#         print("making a phone call....!",mobile_name)
#     def browsing(self):
#         print("you are browsing....",self.bn)
#     def gaming(self):
#         print(" you are playing games")
# #syntax
# #objname = classname()
# obj = mobile_phone()
# obj.calling("samsung")
# obj.browsing() 
# obj.gaming() 

# samsungss22 = mobile_phone()
# samsungss22.calling("s22")
# samsungss22.gaming()

# samsung_s25 = mobile_phone()
# samsung_s25.calling("s25")


# class car():
#     def __init__(self,bn,color,model,eng_v):
#         self.bn=bn
#         self.color = color
#         self.model = model
#         self.eng_v = eng_v
#     def driving(self):
#         print(f"you are driving {self.bn} car")
#     def engine(self,a):
#         print(f"{self.eng_v} engine {a}",self.model,)
# #objname = classname()
# tata = car("tata","white","nexon","2025")
# tata.driving()
# tata.engine("500cc")
# maruthi = car("maruthi","black","brezza","2024")
# maruthi.engine("1000cc")



# class mobile_phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def send_message(self,number,message):
#         print(f" sending {message} to {number} {self.brand} {self.model}")
# class smart_phone(mobile_phone):
#     def browsing(self):
#         print(f"browsing internet on {self.brand} {self.model}")
#     def app(self,appname):
#         print(f"using {appname} app on {self.brand} {self.model}")
# apple = smart_phone("apple","iphone15")
# apple.make_call(123456)
# apple.send_message(123456,"hello")
# apple.browsing()
# apple.app("instagram")


# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
#     def outputChild(self):
#         print('this is child class')  
# obj = Child()
# obj.output()
# obj.outputf()
# obj.outputChild()



# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")
# obj = b()
# obj.parent()
# obj.child1()

# obj2 =c()
# obj2.parent()
# obj2.child2()



# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")
# obj = child()
# obj.father()
# obj.mother()
# obj.child()





class ATM():
    def __init__(self,bankname,location):
        self.bankname = bankname
        self
    def credit(self)
        pass
    def withdraw(self)
        pass

class ATM2(ATM):
    def balance(self)
        pass
    def ministatement(self):
        pass
    def pinchange(self):
        pass





