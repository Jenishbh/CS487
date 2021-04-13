from os import remove


class login:
    
    def login(self,user_id, password):
        return True

    def signup():
        name=input("Enter First Name: "), input("Enter Last Name: ")
        phone:range(10)=int(input("Enter Phone Number: "))
        email=input("Enter Email id: ")

        user_id=(input("Enter uniq User id: "))
        password = None
        userinfo=name,phone,email
        return userinfo

    def add_vehicle():
        while KeyboardInterrupt:
            
            print("1: add vehical\n2: remove vehical\n3: show vehical list\n 4: Exit")
            user=int(input("Enter your choice"))
            if(user==1):
                Vehical_make=input("Enter Vehical Company: ")
                Vehical_model=input("Enter Vehical model: ")
                Vehical_year:range(4)=int(input("Enter a year: "))

                car=Vehical_make,Vehical_model,Vehical_year
                f=open("Vehical_list", 'w')
                f.write(car)
                f.close()
                return car

            elif(user==2):
                pass
            elif(user==3):
                f=open("Vehical_list", 'r')
                print(f.read)

            elif(user==4):
                break
            else:
                return "Error"

class Booking(login):

    
    def slot_Booking():
        pass

    def add_problem():
        pass


class chk_stutas():

    def statud():
        
    


                
                
                



    

    