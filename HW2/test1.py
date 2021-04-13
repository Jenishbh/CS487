
from Hw2 import*

def main():
        time=Time(12,8,12)
        st=SavingsAccount(1.5,5000,time)
        time1=Time(12,15,45)
        st1=SavingsAccount(1.5,10000,time1)
        print("\nIntial Balance")
        print("Serve 1:");st.InitBalance() 
        print("Serve 2:");st1.InitBalance()
       
        print("\n")
        
        print("Serve 1:");st.Show("12:25:12")
        print("Serve 2:");st1.Show("12:35:35")


        st=SavingsAccount(3,5006.25,time)
        st1=SavingsAccount(3,10012.5,time1)
       
        print("\n")
        
        print("Serve 1:");st.Show("7:45:12")
        print("Serve 2:");st1.Show("2:14:55")

main()