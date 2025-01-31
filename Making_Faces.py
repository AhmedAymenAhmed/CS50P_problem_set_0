#in this problem we want to convert :D to 😃  and :( to  😞
#first take input form the user
faces =input("Are you happy or sad? \n")
#we can use replace with unicodes but i prefere using the emoji it self
faces=faces.replace(":D","😃")
faces=faces.replace(":(", "😞")
print(faces)