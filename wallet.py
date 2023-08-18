from web3 import Web3
import time

# Connect to Ganache
ganache_url = "https://sepolia.infura.io/v3/087c45ae45bf42bc91c8b07e02fd5d4d"  # Ganache's default URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

class Account():
    def __init__(self):
        self.account = web3.eth.account.create()
        self.address = self.account.address
        # self.privateKey = self.account.key.hex()

class Wallet():
    def __init__(self):
        self.accounts = []

    def checkConnection(self):
        if web3.is_connected():
           return "Connected"
        else:
            return "Failed to Connect "
    
    def getAvailableAccounts(self):
        accounts = web3.eth.accounts
        for address in accounts:
            balance = self.getBalance(address)
            data = {
                "address" : address,
                "balance" : balance
            }
            self.accounts.append(data)
        return self.accounts
    
    # Check the balance of an Ethereum address
    def getBalance(self, address):
        balance = web3.eth.get_balance(address)
        return web3.from_wei(balance, 'ether')

    # Adding account to old available accounts list  
    def addAccount(self, newAccountAddress):
        balance = self.getBalance(newAccountAddress)
        data = {
            "address" : newAccountAddress,
            "balance" : balance
            }
        self.accounts.append(data)

        return self.accounts

    # Transaction between sender and reciver
    def makeTransactions(self, senderAddress, reciverAddress, amount):
        # Send a small amount of Ether to the new account
        tnxHash = web3.eth.send_transaction({
            "from": senderAddress,
            "to":reciverAddress,
            "value": web3.to_wei(amount, "ether")  # Sending 1 Ether
        })
       
    # Transaction between sender and reciver
    def getTransactions(self, address):
        latestBlockNumber = web3.eth.block_number
        allBlockTranactionHashes = []
        for i in range(latestBlockNumber, 0, -1):
            blockData = web3.eth.get_block(i)
            for tnxHash in blockData["transactions"]:
                allBlockTranactionHashes.append(tnxHash.hex())
        transactionCount = web3.eth.get_transaction_count(address)
        accountTransactions =[]
        for tnxHash in allBlockTranactionHashes:
            transaction = web3.eth.get_transaction(tnxHash)
            if(transaction["from"] == address or transaction["to"] == address):
                tnxType = 'Received'
                if(transaction["from"] == address):
                    tnxType = "Sent"

                accountTransactions.append({
                    "from": transaction["from"],
                    "to" : transaction["to"],
                    "value": web3.from_wei(transaction["value"], "ether"),
                    "tnxHash" : transaction["hash"].hex(),
                    'tnxType' : tnxType
                })
        # print("Total Transactions Count:",transactionCount)
        # print("All transactions:",len(accountTransactions))
        # print("\n")
        return accountTransactions
            
        return transactions
        # Initial list of accounts
        # initial_accounts = web3.eth.accounts.copy()

        # # Continuously check for new accounts
        # while True:
        #     current_accounts = web3.eth.accounts.wallet()

        #     # Compare lists to find new accounts
        #     new_accounts = [address for address in current_accounts if address not in initial_accounts]
        #     print("jj")
        #     if new_accounts:
        #         print("New Accounts Added:")
        #         for address in new_accounts:
        #             balance = web3.eth.get_balance(address)
        #             balance_ether = web3.from_wei(balance, 'ether')
        #             print("Address:", address)
        #             print("Balance:", balance_ether, "ETH")
        #             print("---------------")

        #         # Update initial_accounts to track future changes
        #         initial_accounts = current_accounts

        #     # Add a delay before checking again (in seconds)
           
        #     time.sleep(2)

    
        # pKey = web3.eth.account.create().address
        # print(web3.eth.accounts)
        # # address = web3.eth.account.privateKeyToAccount(privateKey).address
        
        # print("New Account Created:")
        # print("Address:", new_account.address)
        # print("Private Key:", new_account.key.hex())
       

    
