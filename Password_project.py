import random   

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symboles=['!','@','#','$','%','&','*','(',')','+']

print("Welcome To Password Generator!\n")

n_letters=int(input("How Many letters you want in your Password\n"))     #4
n_symboles=int(input("How Many symboles you want in your Password\n"))
n_numbers=int(input("How Many numbers you want in your Password\n"))

# password=""  NOrmal [password] genrete thay 3 letters then 3 symbloes then 3 number atle jetlu input mango tetlu but sequence ma made
password_list=[]   # list ma convert karo to tamne suffel karva made je rendom no biltin function che je tamne alag alag squence ma password genrate kari ne apse

for i in range(1,n_letters+1):               # 1,2,3,4
    char=random.choice(letters)
    password_list += char

for i in range(1,n_symboles+1):
    char=random.choice(symboles)
    password_list+=char

for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char

print("Password in list:- ",password_list)
random.shuffle(password_list)
print("Suffel Password for Password list:- ",password_list)

password=""
for char in password_list:
    password+=char
print("Your Strong Password:-",password)