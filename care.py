# Python3 code here creating class 
class User: 
	def __init__(self, name, amount): 
  		self.name = name
  		self.amount = amount

	def __repr__(self):   
  		return "User(name={},funds={})".format(self.name,self.amount)


class Old(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)


class Young(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)

# creating list	 
old_list = [] 
young_list = [] 

print("\nL I S T O P E R A T I O N S")
print(" 1. Register your name(old), funds if you want to be taken care of")
print(" 2. Register your name(young), price  if you want to take care")
print(" 3. View the list of Old names and funds")
print(" 4. View the list of Young names and price")

choice = int(input("ENTER YOUR CHOICE (1-5): "))
 
if choice == 1:
    element1 = input("Enter your name: ")
    element2 = int(input("Enter funds  "))
    old_list.append(Old(element1, element2))
    for obj in old_list: 
        print( obj.name, obj.amount, sep ='  ' )
    
    with open("Old_names.txt","a+") as wn :
        for item in old_list:
            wn.write("%s\n" % item)

elif choice == 2:
    element1 = input("Enter your name: ")
    element2 = int(input("Enter price  "))
    young_list.append(Young(element1, element2))
    for obj in young_list: 
        print( obj.name, obj.amount, sep ='  ' )

    with open("Young_names.txt","a+") as wn :
        for item in young_list:
            wn.write("%s\n" % item)

elif choice ==3:
    with open("Old_names.txt","r+") as f :
            print(f.read())
elif choice ==4:
    with open("Young_names.txt","r+") as f :
            print(f.read())
