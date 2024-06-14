from function import Bank
class Banking_System:
    def __init__(self):   # constructor
        data = {99  : {'Name': "Saksham Verma", 'Gender': 'M',     # this is the initial data of the customer in the bank
                      'Date of Birth': '2003-05-09', 'Balance': 99,
                      'PAN': '99999999', "PIN": '9999', 'Account_No': 99,
                      'History': ['Account Created.']} }

        f = 0  # f is to keep while loop iterating until exit is pressed

        while(f == 0):
            print('--------------------------------------------------------------------------')

            k = int(input('''                      Type 1 : To Register new Person
                      Type 2 : To Credit Money
                      Type 3 : To Withdraw Money
                      Type 4 : To Delete an Account   
                      Type 5 : To Print Transaction History
                      Type 0 : To Exit     :-  '''))

            if( k == 1):
                acc,dic = Bank.register(self)  # callig the register function from bank class
                if(acc != 0):
                    data[acc] = dic  # updating the data , adding the new customer
                    Bank.detail(data,acc)   # displaying the data of new customer


            elif (k == 2):
                data = Bank.credit(data)

            elif(k == 3) :
                data = Bank.withdraw(data)

            elif(k == 4) :
                data = Bank.delete(data)

            elif(k == 5):
                Bank.get_receipt(data)

            elif(k == 0):
                f = 1  # to exit the Banking system
            else:
                print('Wrong Input !!!    Type the Correct Number  ')




if __name__ == "__main__":
    print('Welcome to the Banking System. ')
    ver = { 'saad' :'99' , 'OMG' : '77'}
    u = input('Enter the Username : ')
    p = input('Enter the Password : ')
    if( u in ver and ver[u] == p ):    # here is the login condition for bankers
        print('Verification Successful ! ')
        start = Banking_System()  # if the authentication is correct then it will start the banking system
    else:
        print("Invalid username or password. Access denied.")


