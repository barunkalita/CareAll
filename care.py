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
request_list= []
approval_list= []

print("\nREGISTRATION | VIEW  |  TICKETING |  FINAL_LIST")
print(" 1. Register your name(retired) and funds if you want to be taken care of")
print(" 2. Register your name(young), price  if you want to take care")
print(" 3. View the list of registered CareSeeker person and funds")
print(" 4. View the list of registered CareTakers and price")
print(" 5. Selection and Approval of caretakers")
print(" 6. Final Approved List")

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
                print("\nPlease select by typing in the name for approval request ")
                print("\nENTER UPTO FOUR NAMES  WHEN PROPMTED\n")
                i=0
                while(i<4):
                    input1 = input("Enter  name : ")
                    with open("Retired_names.txt","r+") as f :
                        if input1 in f.read():
                            print("Request Recorded against your Registered name")
                            request_list.append(input1)
                            with open('request.txt',"a+") as wn :
                                    wn.write("\n%s<------>%s" %(input1,item))
                                    i+=1
                        else:
                            print("No such record found. Try again")
                
                    
            else:
                print("Your name is not in Registered list")
        

      
    elif option ==2:
        item = input("Please Enter your registered name: ")
        with open('Retired_names.txt') as f:
            if item in f.read():
                print("\n...................WELCOME TO APPROVAL PORTAL...............")
                print("\n\nList of CareTaker  who have opted for approval........\n")
                with open("request.txt","r+") as fp :
                    if item in fp.read():
                        with open("request.txt","r+") as fp :
                            print(fp.read())
                        input1 = input("Enter  the caretaker name for approval : ")
                        approval_list.append(input1)
                        with open('approve.txt',"a+") as wn :
                            wn.write("%s----->%s\n" %(item,input1))
                    else:
                        print("CareTaker pending...Please check after sometime")
                
            else:
                print("Your name is not in Registered list")

elif choice ==6:
    with open("approve.txt","r+") as f :
        print(f.read())