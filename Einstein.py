#In this problem we want to take from the user the mass of some thing
#don't forget to make it int
flag ="yes"
while flag=="yes" :
    m=input("Enter the mass ")
    try :
        m=int(m)
        flag="no"
    except ValueError:
        print("Enet a number please")
        flag="yes"
#then give the value of C
C= 300000000 
#then calc E=mc^2
E=(m*C*C)
print("E equal",E)