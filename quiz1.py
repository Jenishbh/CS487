def validateID(this_id,l):                  #String and reverse string

                                           
   checksum = 0                             # initial chksum variable
   n = int(this_id)                         # convert str to int and pass to n variable
   count=1                                  # count for counting
   while(n!=0):                             #start while loop for calculate and scanning one by one number 
       d=int(n%10)                          #start left to right by grabbing last number and convert to int
       if(d%2==1):                          # chk if the int is odd
           c=d*2                            # if int is odd then they will be doubled
           if(c>9):                         # chk if it greater then 9 or not
                g=l[0]                      #grab first index(position) number from reverse list
                checksum=checksum+d+g       #add previous number + currunt number + leftmost digit 
                
           else:                            # if the int is odd but less then 9
               while(d!=0):                 #chk if the number is not 0
                   x = int(d%10)            # start left to right by grabbing last number and convert to int
                   checksum = checksum + x  #add previous number + currunt number
                   d=int(d/10)              # Go to next left number
       else:                                # for even number
                 
           checksum=checksum+d              #add previous number + currunt number
       count=count+1                        # count +1
       n=int(n/10)                          # Go to next left number
   

   return  checksum                         #Return total value of checksum

def main():

   test_id = input("Enter your number")     # User enter a number
   o=int(test_id)                           #convert str to int
   l=[]                                     #l=list
   while o >0:                              #convert str input to list
                    l.insert(0, o%10)
                    o=(o-o%10) // 10
   
   checksum = validateID(test_id,l)         #pass the value to class
   
   print(" Your checksum is "+str(checksum))    #print outpur
   

  
   return

if __name__ == '__main__':
   main()