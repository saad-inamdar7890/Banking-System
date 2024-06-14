import person


class Bank : # created the bank class which has all the required function
    def register(self):
       obj = person.Person()   #   making person object to store all its detail
       if obj.age < 18:  # if age is less than 18 then the acc is not created
           print('Your age is less than 18 , cannot open Bank Account .')
           return 0, {}
       else:
            dic = { 'Name': obj.name , 'Gender': obj.gender ,
                    'Date of Birth': obj._DOB , 'Balance': obj.balance,
                    'PAN': obj._PAN_no , "PIN": obj.PIN , 'Account_No': obj.Acc_No ,
                    'History': ['Account Created.']
            }
            return obj.Acc_No,dic # passing the acc_no as key and dictionary as value for the nested data dictionary

    def delete(dic):  # deleting the account from the data
        acc = int(input('Enter the Account Number to be Deleted: '))
        if acc in dic:
            del dic[acc]
            print('The account is successfully deleted')

        else:
            print('Account not found.')
        return dic


    def credit(dic):  # crediting the money in account
        acc = int(input('Enter the Account Number to be Credited: '))
        if acc in dic:
            c = float(input('Enter the Amount to credit in Rupees: '))
            dic[acc]['Balance'] += c
            print(f'The credit in the account is successful. New Balance: {dic[acc]["Balance"]}')
            dic[acc]['History'].append(f'Amount {c} credited to the account. New Balance: {dic[acc]["Balance"]}')  # here the statement is added to the tranction history of the acc.
        else:
            print('Account not found.')
        return dic


    def withdraw( dic):
        acc = int(input('Enter the Account Number to be Withdrawn: '))
        if acc in dic:
            w = float(input('Enter the Amount to withdraw in Rupees: '))
            if dic[acc]['Balance'] < w:  # when the balance is not enough to withdraw money
                print("Not Enough Balance")
            else:
                dic[acc]['Balance'] -= w
                print(f'The withdrawal from the account is successful. New Balance: {dic[acc]["Balance"]}')
                dic[acc]['History'].append(f'Amount {w} withdrawn from the account. New Balance: {dic[acc]["Balance"]}') # here the statement is added to the tranction history of the acc.
        else:
            print('Account not found.')
        return dic

    def detail ( dic ,acc): # printing the account detail
         if acc in dic:
            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print(f'Name: {dic[acc]["Name"]}')
            print(f'Gender: {dic[acc]["Gender"]}')
            print(f'Date of Birth: {dic[acc]["Date of Birth"]}')
            print(f'Balance: {dic[acc]["Balance"]}')
            print(f'PAN: {dic[acc]["PAN"]}')
            print(f'PIN: {dic[acc]["PIN"]}')
            print(f'Account No.: {acc}')
            print(f'History: {", ".join(dic[acc]["History"])}')
            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
         else:
            print('Account not found.')

    def get_receipt(dic):  # printing the transacton history
        acc = int(input('Enter the Account Number : '))
        if acc in dic:
            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
            print('History:')
            for entry in dic[acc]['History']:
                print(f'  - {entry}')
            print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

        else:
            print('Account not found.')






