from flask import Flask, render_template, request
import os
from time import time
from wallet import Wallet
from wallet import Account


STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

# Creating new Wallet
myWallet =  Wallet()

@app.route("/", methods= ["GET", "POST"])
def home():
    global myWallet

    # Checking the connection with API
    isConnected = myWallet.checkConnection()

    # Getting avaliable accounts and their balance
    accounts  = myWallet.getAvailableAccounts()
   

    if request.method == "GET":
        transactions = myWallet.getTransactions(accounts[0]['address'])

        # return allprices as second parameter
        return render_template('index.html', isConnected=isConnected, accounts=accounts, transactions = transactions, senderAddress = accounts[0]['address'], balance = accounts[0]['balance'])
    else:
        senderAddress = request.form.get("senderAddress")
        receiverAddress = request.form.get("receiverAddress")
        amount = request.form.get("amount")
        
        myWallet.makeTransactions(senderAddress, receiverAddress, amount)

        transactions = myWallet.getTransactions(senderAddress)
        balance = myWallet.getBalance(senderAddress)
    

        return render_template('index.html', isConnected=isConnected, accounts=accounts, transactions = transactions, senderAddress = senderAddress, balance = balance)
    

@app.route("/changeAddress", methods= ["GET", "POST"])
def changeAddress(): 
    global myWallet
    newSenderAddress = request.args.get("address")
    transactions = myWallet.getTransactions(newSenderAddress)

    # Checking the connection with API
    isConnected = myWallet.checkConnection()
    # Getting avaliable accounts and their balance
    accounts  = myWallet.getAvailableAccounts()

    balance = myWallet.getBalance(newSenderAddress)
    
    return render_template('index.html', isConnected=isConnected, accounts=accounts, transactions = transactions, senderAddress = newSenderAddress, balance = balance)



# C97 
# Create Ganache account and setup locally
# Show all the available accounts and get the balance of the account
# Generate the New Account address and Private Key and get balance of newly created account


# C98
# Do transction between two address
# Do Transactions between newely created account
# Show all the transaction on the web


if __name__ == '__main__':
    app.run(debug = True, port=5001)
