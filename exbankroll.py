import datetime

nowrl = datetime.datetime.now()
now = nowrl.strftime("%B %d %Y %I:%M %p")

userslist = []
passeslist = []
tokenlist = []
token = 0
defaultbalance = 0
defaultbalancelist = []
log = []

def trade():
    global token, tokenlist, defaultbalance, defaultbalancelist
    print("you can only trade with one account at a time. we are working on making a feature to correct this. please be patient with us!")
    tradee = input("what is the token number of the account you would like to send money to? ")
    tradee = int(tradee)
    if tradee in tokenlist:
        money = float(input("how much would you like to send? please give in decimal format: $"))
        print(f'to confirm, you would like to send ${money} to account number {tradee}.')
        confirm = input("type 'yes' to confirm: ")
        if confirm == "yes":
            sender = tokenlist.index(token)
            receiver = tokenlist.index(tradee)
            senderbalance = defaultbalancelist[sender]
            receiverbalance = defaultbalancelist[receiver]
            senderbalance -= money
            receiverbalance += money
            senderbalance = defaultbalancelist[sender] 
            receiverbalance =  defaultbalancelist[receiver] 
            print(f'account number {token} now has ${senderbalance}')
            print(f'account number {tradee} now has ${receiverbalance}')
            statement = f'{now}: {token} has transferred {tradee} ${money}; {token} balance {senderbalance}, {tradee} balance, {receiverbalance}'
            log.append(statement)
        else:
            print("okay, transaction canceled.")
    else:
        print('sorry, that account number is not currently enrolled with us.')

def deposit():
    global token, tokenlist, defaultbalance, defaultbalancelist
    balanceadd = float(input("what is the balance you wish to add? please give in decimal format: $"))
    print(f'to confirm, you would like to deposit ${balanceadd} into your account.')
    confirm = input("type 'yes' to confirm: ")
    if confirm == "yes":
        depositee = tokenlist.index(token)
        defaultbalancelist[depositee] += balanceadd  
        newbalance = defaultbalancelist[depositee]
        statement = f'{now}: account number {token} has added a deposit of ${balanceadd}. their new balance is ${newbalance}'
        log.append(statement)
        print(f'account number {token} now has ${newbalance}')
    else:
        print("okay, transaction canceled.")

def accountview():
    global token, tokenlist, defaultbalancelist
    accountnumber = input("what is the account number? ")
    accountnumber = int(accountnumber)
    if accountnumber in tokenlist:
        index = tokenlist.index(accountnumber)
        balance = defaultbalancelist[index]
        print(f'account number {accountnumber} has a balance of ${balance}')
        statement = f'{now}: {token} viewed the balance for account number {accountnumber}, which is ${balance}'
        log.append(statement)
    else:
        print("sorry, that account does not exist")

def login():
    global token, tokenlist, defaultbalance, defaultbalancelist
    username = input("username: ")
    password = input("password: ")
    if username in userslist:
        index = userslist.index(username)
        if passeslist[index] == password:
            token = tokenlist[index]
            print(f'welcome {username}, your account number is {token}')
            tradeask = input("do you want to send someone else money right now? ")
            if tradeask == "yes":
                trade()
            viewask = input("do you want to view your account balance? ")
            if viewask == "yes":
                accountview()
            depoask = input("do you want to make a deposit? ")
            if depoask == "yes":
                deposit()
            else:
                print("ok, have a nice day!")
        else:
            print("wrong password.")
    else:
        userslist.append(username)
        passeslist.append(password)
        token += 1
        tokenlist.append(token)
        defaultbalancelist.append(defaultbalance)
        print(f"congratulations on signing up! Your token number is {token} and your current balance is ${defaultbalance}")
        statement = f'{now}: {username} assigned account number {token}'
        log.append(statement)
