import hashlib
accountdict = {"ID": ["username", "password"]}
class SignUp:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    def __repr__(self):
        return self.id

def hashtest(password):
    hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hash

user1 = SignUp(1,"Philip", "1234abcd")
user2 = SignUp(2,input("Enter a username: "), input("Enter a password: "))
test1 = hashtest(input("Confirm Password: "))

#Creating accounts to txt file
#def appendaccounts(user):
    #if user.password == test1:
        #with open("accounts.txt", "a") as accounts:
            #accounts.write(user)

#Creating accounts to a dictionary
def appenddictionary(user):
    if user.password == test1 and user.username not in accountdict:
        accountdict[user.id] = [user.username, user.password]
appenddictionary(user1)
appenddictionary(user2)

print(user1.username, user1.password)
print(user2.username, user2.password)
print("Compare this hash with output above:", test1)
print(accountdict)
