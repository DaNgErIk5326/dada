# login = input("Enter your Email: ")
# password = input("Enter your password: ")
right_login = "DaNgErIk"
right_password = 125 #z dvoh cifr

for h in range(10):
  for t in range(10):
    for f in range(10):
      pas = h*100 + t*10 + f
      print(pas)
      if pas == right_password:
        print("ACCESS GRANTED! Pass: ", pas);
        break
  if pas == right_password:
    print("ACCESS GRANTED! Pass: ", pas);
    break
if pas == right_password:
  break
