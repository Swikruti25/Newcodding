#DAY4-->16/03/23
#Question1
'''def nearest_palindrome(number):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    i = number + 1
    while True:
        if is_palindrome(i):
            return i
        i += 1
print(nearest_palindrome(99))
print(nearest_palindrome(1221))'''

#OR
'''import sys
def nearest_palindrome(number):
    for i in range(number+1,sys.maxsize):
     if str(i) == str(i)[::-1]:
        return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))'''

#Question2
'''def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality

patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}

print(max_visited_speciality(patient_medical_speciality_list,medical_speciality))'''

#Question3



















#OOPS concept in python
#Calculate the output:
#1
'''class Example:
    def __init__(self,num):
       self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())'''

#2
'''class Customer:
    def __init__ (self):
        cust_id = 100
c1=Customer()
print(c1.cust_id)'''


#3
'''class Customer:
    def __init__(self,id):
        self.id=100
c1=Customer(200)
print(c1.id)'''

#4
'''class Customer:
    def __init__(self,id):
        self.id= id
c1=Customer(200)
print(c1.id)'''


#5
'''class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn python the hard way"

my_fav.title="Learning python"

print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)'''

#6
'''class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s1=Shoe(1000,"Canvas")
print(s1)
print(s1.price,s1.material)
print("the unique id of the object",id(s1))'''

#Q7
'''class Shoe:
         def __init__(self,price,material):
             self.price = price
             self.material = material

         def __str__(self):
             return "Shoe with price:" + str(self.price) + "and material:" + self.material
S1=Shoe(1000,"Canvas")
print(S1)'''

#Q8
'''class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("calculating price")
Mobile().purchase()'''

#Q9
'''class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand == "Redmi":
            discount = 10
        else:
            discount=5
        self.total_price=self.price-self.price * (discount/100)
        print("Total price of",self.brand,"mobile is",self.total_price)
mob1=Mobile("Redmi",20000)
mob2=Mobile("Realmi",10000)
mob1.purchase()
mob2.purchase()'''

#Q7
'''class Customer:
             def __int__(self,cust_id,name,age,wallet_balance):
                         self.cust_id = cust_id
                         self.name = name
                         self.age = age
                         self.wallet_balance = wallet_balance
             def update_balance(self,amount):
                if amount < 1000 and amount> 0:
                    self.wallet_balance += amount
             def show_balance(self):
                print("The balance is",self.wallet_balance)
c1=Customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()'''


#Q8

'''class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("dam name:",dam1.name)
print("dam length",dam1.get_length())'''

#Q9

'''class Table:
    def __init__(self):
        self.no_of_leg=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self._glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
           rate=20000
        elif(self.__wooden_top==True):
           rate=30000
        else:
           rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)'''


#Q10
'''class Table:
    def __init_(self):
        self.no_of_leg=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)'''


#DAY5-->17/03/23
#OOPS Concept
#Q1

'''class vehicle:
    def __init__(self,id,type,cost):
        self.__vehicle_id = id
        self.__vehicle_type= type
        self.__vehicle_cost= cost
        self.__vehicle_premium_amount= None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def set_vehicle_premium_amount(self,vehicle_premium_amount):
        self.__vehicle_premium_amount=vehicle_premium_amount
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_vehicle_premium_amount(self):
        return self.__vehicle_premium_amount
    def calculate_premium(self):
        if self.__vehicle_type=="two_wheeler":
            self.__vehicle_premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="four_wheeler":
            self.__vehicle_premium_amount=self.__vehicle_cost*6/100
        else:
            print("invalid")
    def display_details(self):
        print(self.__vehicle_type,self.__vehicle_cost,self.__vehicle_premium_amount)
v=vehicle(11,"two_wheeler",3490)
v.calculate_premium()
v.display_details()'''

#Q2
'''class student:
    def __init__(self):
        self.__student_id=None
        self.__student_age=None
        self.__student_marks=None
    def set_student_id(self,student_id):
        self.__student_id=student_id
    def set_student_age(self,student_age):
        self.__student_age=student_age
    def set_student_marks(self,student_marks):
        self.__student_marks=student_marks

    def get__student_id(self):
        return self.__student_id
    def get__student_age(self):
        return self.__student_age
    def get__student_marks(self):
        return self.__student_marks

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
                return True
        else:
                return False
    def validate_age(self):
        if self.__age>=20:
                return True
        else:
                return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
                if self.__marks>=65:
                     return True
                else:
                     return False
    def display(self):
         print(self.__student_id,self.__student_age,self.__student_marks)

s=student()
s.set_student_id(342)
s.set_student_age(20)
s.set_student_marks(80)
print(s.check_qualification())
s.display()'''

#Q3
types=['small','medium','small','medium']
class customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
    def set_customer_name(self,customer_name):
           self.__customer_name=customer_name
    def set_quantity(self,quantity):
           self.__quanity=quantity
   #def get_customer_name(self,customer_name):
         # return self.__customer_name
    #def get_quantity(self,quantity):
         # return self.__quantity
    def validate_quantity(self):
          if self.__quantity in range(1,6):
                  return True
          else:
                  False
class pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
             return False
            
    def calculate_pizza_cost(self):
      if self.validate_pizza_type() and customer.validate_quantity(self.__customer):
        if self.__pizza_type.title()=="small":
           self.pizza_cost=150* customer.get_quantity(self.__customer)
        if self.__additional_topping:
            self.pizza_cost+=35 * customer.get_quantity(self.__customer)

        if self.__pizza_type.title()=="Medium":
         self.pizza_cost=200*customer.get_quantity(self.__customer)
        if self.__additional_topping:
            self.pizza_cost+=50*customer.get_quantity(self.__customer)
        if not self.__service_id:
             self.__service_id = self.__pizza_type(0) + str(pizzaservice.counter+1)
             pizzaservice.counter+=1
        else:
             self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(pizzaservice): 
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms= distance_in_kms
        pizzaservice__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
         if self.validate_distance_in_kms():
             pizzaservice.calculate_pizza_cost(self)
             if self.pizza_cost!=-1:
                 distance=1
             while(distance<=self.__distance_in_kms):
                 if distance in range(1,6):
                    self.pizza_cost += 5
                 if distance in range(6,11):
                     self.pizza_cost +=7
                     distance+=1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
c=customer("Asha",5)
p1 = pizzaservice(c,"MEDIUM",True)
p1.calculate_pizza_cost()
print(p1.get_service_id())

d1=Doordelivery(c,"MEDIUM",True)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())





                     
                 
    

            









