""" This program is take the user name as input
    and to print out Hello "username" """

# hello program
def hello(user):
    print("Hello " + user + "!!!")

# main starts from here
def main():
    name = input("Enter your name : ")
    hello(name)
main()