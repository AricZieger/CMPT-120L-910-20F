from typing import Tuple
savings = 1096.25
checking = 1590.80

def process_transaction(transaction):
    global checking
    global savings
    if transaction > 0:
        checking += (transaction * 0.85)
        savings += (transaction * 0.15)
    elif transaction < 0:
        checking += transaction
    else:
        print("There was no change made to your account for a transaction.")

def saturdays_bank_transactions(transactions) -> Tuple[float, float]:
    for charge in transactions:
        process_transaction(charge)

    return checking, savings

if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transations)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))