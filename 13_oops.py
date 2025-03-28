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





# class ATM():
#     def __init__(self,bankname,location):
#         self.bankname = bankname
#         self
#     def credit(self)
#         pass
#     def withdraw(self)
#         pass

# class ATM2(ATM):
#     def balance(self)
#         pass
#     def ministatement(self):
#         pass
#     def pinchange(self):
#         pass





############## march  24 2025  ########################
#polymorphism ---> implementing same thing in different forms
#1.overloading  --> 1.operator overloading 2.method overloading
#2.overriding --> method overiding


# "+" --> operator overloading
# a = 10
# b = 20
# print(a+b)


# a = "10"
# b = "20"
# print(a+b)



# 2.method overloading --->
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments

# class calculator():
#     def add(self,a,b):
#         print(a,b)
#     def add(self,a,b,c):
#         print(a,b,c)
# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add(10,10,"vasu")
# obj.add(10,"vasu")


# method name should be same
# arguments must be different ---> in the terms of length or type of arguments
# class calculator():
#     def add(self,a=None,b=None,c=None,d=None):
#         print(a,b,c,d)
# obj = calculator()
# obj.add(10,10,10,10)
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add()
# obj.add("vasu","charisma","samuel","pavan")
# obj.add("vasu","charisma","samuel",)
# obj.add(5.7,6.7,8.7,"srikanth")


# 2.method overriding--> method name should be same, arguments should be also same
# class father():
#     def details(self,a):
#         print("this is base class",a)
# class child(father):
#     def details(self,a):
#         print("this is child class",a)
#         super().details("200cr")
# obj = child()
# obj.details("100cr")



# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _
# class Gfather():
#     def __init__(self,a):
#         self._a = a
#         print(a)
#     def sample(self):
#         print(self._a)
# class father(Gfather):
#     def display(self):
#         print(self._a)
# obj = father("100cr")
# obj.display()
# obj.sample()



# class Gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(a)
#     def sample(self):
#         print(self.__a)
#     def sample_2(self):
#         print(self.__a)
# class father(Gfather):
#     def display(self):
#         print(self.__a)
# obj = father("100cr")
# obj.display()
# obj.sample()


# class bms():
#     def userlogin(self):
#         pass
#     def account(self):
# class money(bms):
#     def with(self):
#         pass
#     def deposit(self):
#         pass





# class gf():
#     def __init__(self,pin):
#         self._pin = pin
#         print(self._pin)
# class c2(gf):
#     def sample(self):
#         print(self._pin)
#     def sample2(self):
#         pass
# class c3(gf):
#     def sample3(self):
#         print()





#abstraction --> hiding the implementation and showing only essential part

# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module

# from abc import ABC, abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print("implementing in derived class")
#     def display2(self):
#         print("implementing in derived class display2")
# obj = demo()
# obj.display()
# obj.display2()










# from abc import ABC, abstractmethod   
# class Car(ABC): 
#     @abstractmethod  
#     def mileage(self):   
#         pass  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
#     def smartfeaturs(self):
#         print("providing additional functionalities")
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ") 
# obj = Tesla()
# obj.mileage()
# obj2 = Suzuki()
# obj.mileage()