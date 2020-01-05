#Super Class
class User: 
	def __init__(self, name, amount): 
  		self.name = name
  		self.amount = amount

# Sub Class
class Retired(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)
    def __repr__(self):   
  	    return "(name={},budget={})".format(self.name,self.amount)

# Sub Class
class Young(User):

    def __init__(self, name,amount):
        super().__init__(name,amount)
    def __repr__(self):   
  	    return "(name={},fees={})".format(self.name,self.amount)


# creating list	 which will help to store the data locally in file
retired_list = []     
young_list = []
request_list= []
approval_list= []
import shutil
print("\nREGISTRATION | VIEW  |  TICKETING |  FINAL_LIST")
print(" 1. Register your name(retired) and funds if you want to be taken care of")
print(" 2. Register your name(young), price  if you want to take care")
print(" 3. View the list of registered CareSeeker person and funds")
print(" 4. View the list of registered CareTakers and price")
print(" 5. Selection and Approval of caretakers")
print(" 6. View Approval Pending list for caretakers")
print(" 7. Final Approved List of Caretakers")
print(" 8. Reviews and Ratings")

choice = int(input("ENTER YOUR CHOICE (1-8): "))
 
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
    print("\n......Registered Retired person with allocated budget......\n")
    with open("Retired_names.txt","r+") as f :
            print(f.read())
elif choice ==4:
    print("\n.....Registered Young person with fees........\n")
    with open("Young_names.txt","r+") as f :
            print(f.read())


elif choice ==5:
    print("\n........Ticket options.........\n\n")
    print(" 1. Selecting retired person you wish to take care of")
    print(" 2. Approving young person you wish to be taken care by\n")
    option= int(input("ENTER YOUR CHOICE (1-2): "))
    if option == 1:
        item = input("Please Enter your registered name(Young): ")
        with open('Young_names.txt') as f:
            if item in f.read():
                print("\n...................WELCOME TO REQUEST PORTAL...............")
                print("\n\n.................List of Retired person with allocated budget........\n")
                with open("Retired_names.txt","r+") as f :
                    print(f.read())
                print("\nPlease select by typing in the name for approval request ")
                input1 = input("Enter  name : ")
                with open("Retired_names.txt","r+") as f :
                    if input1 in f.read():
                        print("Request Recorded against your Registered name")
                        request_list.append(input1)
                        with open('request.txt',"a+") as wn :
                            wn.write("\n%s: <-----------> %s" %(input1,item))
                    else:
                        print("No such record found. Try again")
            
                    
            else:
                print("Your name is not in Registered list")
        

      
    elif option ==2:
        item = input("Please Enter your registered name(Retired): ")
        with open('Retired_names.txt') as f:
            if item in f.read():
                print("\n...................WELCOME TO APPROVAL PORTAL...............")
                print("\n\nList of CareTaker  who have opted for approval........\n")
                with open("request.txt","r+") as fp :
                    if item in fp.read():
                        with open("request.txt","r+") as fp :
                            print(fp.read())
                        input1 = input("Enter  the caretaker name  listed against your name in the above list for approval : ")
                        approval_list.append(input1)
                        with open('approve.txt',"a+") as wn :
                            wn.write("%s is taken care by : %s\n" %(item,input1))
                        with open("AssignedCaretaker.txt","a+") as op:
                            op.write("%s is taking care of %s\n" %(input1,item))
                        with open("request.txt", "rt") as fin:
                            with open("test.txt", "wt") as fout:
                                for line in fin:
                                    fout.write(line.replace(item, 'Already Assigned'))
                        shutil.copyfile('test.txt', 'request.txt',follow_symlinks=True)

                    else:
                        print("Waiting for a Caretaker to sign up against your name...Please check after sometime")
                
            else:
                print("Your name is not in Registered list")

elif choice ==6:
    print("\n.......Approval Pending list.........\n")
    with open("request.txt","r+") as f :
            print(f.read())

elif choice ==7:
    print("\n........FINAL LIST.........\n\n")
    print(" 1. View the List of Approved Caretakers")
    print(" 2. View the List of Careseeker along with the approved Caretaker\n")
    ch= int(input("ENTER YOUR CHOICE [1-2]: "))
    if ch == 1:
        with open("AssignedCaretaker.txt","r+") as f :
            print(f.read())
    if ch == 2:
        with open("approve.txt","r+") as f :
            print(f.read())

if choice ==8:
    print("\n Reviews and Ratings.....\n")
    print(" 1. Give Review and Ratings for Caretakers")
    print(" 2. Give Review and Ratings for Careseeker")
    print(" 3. View Review and Ratings\n")
    option= int(input("Enter your choice[1-2]"))
    if option == 1:
        input1 = input("Please Enter your registered name(Retired): ")
        with open('Retired_names.txt') as f:
            if input1 in f.read():
                print("\n...................WELCOME TO RATINGS PORTAL...............")
                input2= input("Enter the name of caretaker for reviews: ")
                with open('Young_names.txt') as f:
                    if input2 in f.read():
                        input3=input("Please give review : ")
                        with open('reviews_young.txt','a+') as q:
                            q.write("Review about %s by %s : %s\n" %(input2,input1,input3))
                    else:
                        print("No caretaker found with the mentioned name")

    if option == 2:
        input1 = input("Please Enter your registered name(Young): ")
        with open('Young_names.txt') as f:
            if input1 in f.read():
                print("\n...................WELCOME TO RATINGS PORTAL...............")
                input2= input("Enter the name of careseeker for reviews: ")
                with open('Retired_names.txt') as f:
                    if input2 in f.read():
                        input3=input("Please give review : ")
                        with open('reviews_retired.txt','a+') as q:
                            q.write("Review about %s by %s : %s\n" %(input2,input1,input3))
                    else:
                        print("No caretaker found with the mentioned name")

    if option == 3:
        with open("reviews_retired.txt","r+") as f :
            print(f.read())
        with open("reviews_young.txt","r+") as f :
            print(f.read())               

