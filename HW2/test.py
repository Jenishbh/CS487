from Hw2 import *

def main():
        time=Time(12,8,12)
        
        print("\nServe 1\n")
        st=SavingsAccount(1.5,5000,time)
        
        st.InitBalance()
        st.Show("12:25:12")

        
        time1=Time(12,15,45)
        print("\nServe 2\n")
        st1=SavingsAccount(3,10000,time1)
        st1.InitBalance()
        st1.Show("12:35:35")

main()