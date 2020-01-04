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

class Request:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "(name={})".format(self.name)

class Approval:
    def __init__(self,name):
        self.name=name

# creating list	 
retired_list = []
young_list = []
request_list= []
approval_list= []

print("\nREGISTRATION | VIEW  |  TICKETING")
print(" 1. Register your name(retired) and funds if you want to be taken care of")
print(" 2. Register your name(young), price  if you want to take care")
print(" 3. View the list of Retired persons and funds")
print(" 4. View the list of Young person and price")
print(" 5. Ticketing")

choice = int(input("ENTER YOUR CHOICE (1-5): "))
 
if choice == 1:
    element1 = input("Enter your name for registraton: ")
    element2 = int(input("Enter budget for allocation  "))
    retired_list.append(Retired(element1, element2))
    for obj in retired_list:
        print("Record succesfully added") 
        print( obj.name, obj.amount, sep ='  ' )
    
    with open("Retired_names.txt","a+") as wn :
        for item in retired_list:
            wn.write("%s\n" % item)

elif choice == 2:
    element1 = input("Enter your name for registration: ")
    element2 = int(input("Enter care fees  "))
    young_list.append(Young(element1, element2))
    for obj in young_list: 
        print("Record succesfully added")
        print( obj.name, obj.amount, sep ='  ' )

    with open("Young_names.txt","a+") as wn :
        for item in young_list:
            wn.write("%s\n" % item)

elif choice ==3:
    print("Registered retired person with allocated budget")
    with open("Retired_names.txt","r+") as f :
            print(f.read())
elif choice ==4:
    print("Registered Caretaker price List for one month care")
    with open("Young_names.txt","r+") as f :
            print(f.read())

elif choice ==5:
    print("\n........Ticket options.........\n\n")
    print(" 1. Selecting retired person you wish to take care of")
    print(" 2. Approving young person you wish to be taken care by\n")
    option= int(input("ENTER YOUR CHOICE (1-2): "))
    if option == 1:
        item = input("Please Enter your registered name: ")
        with open('Young_names.txt') as f:
            if item in f.read():
                print("\n...................WELCOME TO REQUEST PORTAL...............")
                print("\n\n.................List of Retired person with allocated budget........\n")
                with open("Retired_names.txt","r+") as f :
                    print(f.read())
                print("\nPlease select entries for approval by typing in the values")
                ele1 = input("Enter  name : ")
                with open("Retired_names.txt","r+") as f :
                    
                    if ele1 in f.read():
                        print("Request Recorded against your Registered name")
                        request_list.append(Request(ele1))
                        print(request_list)
                        with open(item,"a+") as wn :
                            for item in request_list:
                                wn.write("%s\n" % item)
                    else:
                        print("No such record found. Try again")
                 
                    
            else:
                print("Your name is not in Registered list")
        

      


    # print("Retired person with allocated budget")
    # with open("Retired_names.txt","r+") as f :
    #         print(f.read())
    # input1=input("Enter the name of the retired person:")