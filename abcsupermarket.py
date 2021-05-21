#ABC Supermarket
from datetime import datetime,date
members=["John"]
check_name=input("Enter Your name: ")
def check_bag():
    
    checking_bag=input("Do you have a bag? ")
    if checking_bag=='yes':
        total_slots=[23,34,56,77,7,78,65]
        occupied_slots=[23,65]
        assigned_slot=int(input("Choose a storage slot: ")) 
        for slot in total_slots:
            if assigned_slot not in occupied_slots:                
                occupied_slots.append(assigned_slot)
                print("Storage slot Empty: You can access it ")
                print("Proceed to shopping")
                
                break

            else:
                print("Slot occupied")
                print("Choose another slot")
                break

if check_name not in members:
    print("Looks like you are a new Member. Create Profile: ")
    date_of_birth=input("Enter Date of Birth(YYY-MM-DD): ")

    new_member={
        "name": check_name,
        "D.O.B":datetime.strptime(date_of_birth,"%Y-%m-%d"),
        "I.D":int(input("Enter ID Number: ")),
        "Phone":input("Enter phone number: ")
    }
    members.append(new_member["name"])
    print("You are now a member of our organization ")
    print(members)
    check_bag()

else:
    print("Welcome  {}".format(check_name))
    check_bag()

