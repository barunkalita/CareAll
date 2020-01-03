# Python3 code here creating class 
class User: 
	def __init__(self, name, amount): 
  		self.name = name
  		self.amount = amount

	


class Retired(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)
    def __repr__(self):   
  	    return "(name={},budget={})".format(self.name,self.amount)

class Young(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)
    def __repr__(self):   
  	    return "(name={},fees={})".format(self.name,self.amount)
# creating list	 
retired_list = []
young_list = [] 

print("\nL I S T O P E R A T I O N S")
print(" 1. Register your name(retired) and funds if you want to be taken care of")
print(" 2. Register your name(young), price  if you want to take care")
print(" 3. View the list of Retired persons and funds")
print(" 4. View the list of Young person and price")

choice = int(input("ENTER YOUR CHOICE (1-5): "))
 
if choice == 1:
    element1 = input("Enter your name: ")
    element2 = int(input("Enter budget for allocation  "))
    retired_list.append(Retired(element1, element2))
    for obj in retired_list:
        print("Record succesfully added") 
        print( obj.name, obj.amount, sep ='  ' )
    
    with open("Retired_names.txt","a+") as wn :
        for item in retired_list:
            wn.write("%s\n" % item)

elif choice == 2:
    element1 = input("Enter your name: ")
    element2 = int(input("Enter care fees  "))
    young_list.append(Young(element1, element2))
    for obj in young_list: 
        print("Record succesfully added")
        print( obj.name, obj.amount, sep ='  ' )

    with open("Young_names.txt","a+") as wn :
        for item in young_list:
            wn.write("%s\n" % item)

elif choice ==3:
    print("Retired person with allocated budget")
    with open("Retired_names.txt","r+") as f :
            print(f.read())
elif choice ==4:
    print("Caretaker price List for one month care")
    with open("Young_names.txt","r+") as f :
            print(f.read())
