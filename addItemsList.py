movies=[]
mov1=input("Enter 1st Movie: ")
mov2=input("Enter 2nd Movie: ")
mov3=input("Enter 4rd Movie: ")


movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

movies.sort(reverse=True)
print("Your Favourite's Movies Are: ",movies)