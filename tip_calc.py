#We want to make a program to help clac the tip of any customer
#First we ask for the price of the meal
flag ="yes"
while flag=="yes" :
    price =(input("Enter the meal price "))
    try:
        price=int(price)
        flag="no"
    except ValueError:
        print("Enter a number please")
        flag="yes"
#now we ask for the percentage they will tip
flag="yes"
while flag=="yes" :
    per=(input("Enter the % you will tip "))
    per =per.replace("%","")
    try:
        per =int(per)
        flag="no"
    except ValueError:
        print("Enter a number please")
        Flag="yes"
#print the fintal payment
pay =price +(price*(per/100))
print("you will pay",pay)