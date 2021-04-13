import sys

bookings_holi = dict()
bookings_magic = dict() 
waiting_list = list()

def schedule(): #method to schedule bookings

    cust = input("Enter Customer name: ").upper()

    i=1

    for holi_name in bookings_holi.keys(): #prints all holiday names

        print("%d. %s"%(i, holi_name))

        i=i+1

    holiday = input("Enter a holiday name: ").upper()

    if holiday.upper() not in bookings_holi.keys(): #if invalid holiday name

      sys.exit("No holiday by that name")

    else:

        w = 1

        for magician in bookings_magic.keys():

            if bookings_magic[magician][1] == "":

                print("Booking confirmed: ")

                print("Magician: ", magician)

                print("Holiday: ", holiday)

                print("Customer name: ", cust)

                w = 0

                bookings_magic[magician][0] = cust

                bookings_magic[magician][1] = holiday

                bookings_holi[holiday][0] = cust

                bookings_holi[holiday][1] = magician

                break

        if w==1:    #put into waiting list in case no magician available

            waiting_list.append([cust, holiday])

            print("Customer %s has put into waiting list" %(cust))

def cancel():   #method for canceling booking

    cust = input("Enter Customer name: ").upper()

    i=1

    for holi_name in bookings_holi.keys():

        print("%d. %s"%(i, holi_name))

        i=i+1

    holiday = input("Enter a holiday name: ").upper()

    for wl in waiting_list: #check waiting list for the booking

        if wl[0]==cust and wl[1]==holiday:

            waiting_list.remove(wl)

            print("Removed from Waiting list")

            return

    if holiday.upper() not in bookings_holi.keys(): #if invalid holiday

        sys.exit("No holiday by that name")

    elif bookings_holi[holiday][0] != cust:

        sys.exit("No reservation on this holiday by that name")

    else:

        bookings_magic[bookings_holi[holiday][1]] = ["", ""]

        f=1

        for wl in waiting_list:

            if wl[1] == holiday:

                bookings_magic[bookings_holi[holiday][1]] = [wl[0], wl[1]]

                bookings_holi[holiday] = [wl[0], bookings_holi[holiday][1]]

                f=0
                sys.exit("COnformed Cancel")
                break

        if f==1:

            bookings_holi[holiday] = ["", ""]

   
def status():   #method to show a booking status

    r = int(input("Enter 1 for magician or 2 for holiday"))

    if r==1 :

        m = input("Enter name: ").upper()

        if m.upper() not in bookings_magic.keys():

            sys.exit("No magician by that name")

        if bookings_magic[m.upper()][1] == "":

            print("No booking for that magician so far")

        else:

            print("Magician: ", m.upper())

            print("Booked for Customer:", bookings_magic[m.upper()][0] )

            print("Booked on Holiday:", bookings_magic[m.upper()][1] )

    elif r==2:

        h = input("Enter name: ").upper()

        if h.upper() not in bookings_holi.keys():

            sys.exit("No Holiday by that name")

        if bookings_holi[h.upper()][1] == "":

            print("No booking on that holiday so far")

        else:

            print("Holiday: ", h.upper())

            print("Booked for Customer:", bookings_magic[h.upper()][0] )

            print("Booked Magician:", bookings_magic[h.upper()][1] )

def quit(): #method to quit the program

    sys.exit("Exiting...")

def showMenu(): #method to show menu

    print("1. Schedule\n2. Cancel\n3. Status\n4. Exit\nEnter an option: ")

    r = int(input())

    if r==1:

        schedule()

    elif r==2:

        cancel()

    elif r==3:

      status()

    elif r==4:

        quit()

    showMenu()

def loadLists(holiday, magician):   #method to load magician and holiday list from txt files

    li = list()

    h = open(holiday)

    m = open(magician)

    lines = h.readlines()

    for line in lines:

        line = line.replace("\n", "")

        li.append(line)

        bookings_holi[line.upper()]=["", ""]

    lines = m.readlines()

    for line in lines:

        line = line.replace("\n", "")

        bookings_magic[line.upper()]=["", ""]

def main(): #main method

    loadLists("holidays.txt", "magician.txt")

    showMenu()

if __name__ =="__main__":

    main()

    input()