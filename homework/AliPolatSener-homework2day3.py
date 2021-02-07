#without dict
username, password="polatsener", "p@ssw0rd"

while True :
  user_name=input("Please enter username:")
  pass_word=input("Please enter password:")

  if user_name==username and pass_word==password:
    print("Logged in successfully!")
    break
  else:
    print("Invalid username or password")



#with creating dict
d={username: "polatsener", password:"p@ssw0rd"}

while True :
  user_name=input("Please enter username:")
  pass_word=input("Please enter password:")

  if user_name==username and pass_word==pass_word:
    print("Logged in successfully!")
    break
  else:
    print("Invalid username or password")
