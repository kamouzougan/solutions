balance = 0 
def deposit(num): 
    total  = balance  + amount 
    return total 
def withdraw(num): 
    total = balance - amount 
    return total 





while True:
    print(''' ########################################################''')
    print('                  Welcome to my bank                         ')
    print  ('''  
                       1.deposit
                       2.withdraw 
                       3.check balance) 
                ''')
    menu = input('please make your selection')
    
    if menu == '1': 
        amount = int(input('Please enter your amount') )
        print('deposit')
        balance = deposit(amount)
        print('your total deposit is :',balance)
    if menu == '2':
        amount = int(input('Please enter your amount') )
        print('withdraw')
        balance = withdraw(amount)
        print('after your withraw your total balance is : ', balance)
        print()
    if menu =='3':
       print('Your total balance is : ' , balance)
