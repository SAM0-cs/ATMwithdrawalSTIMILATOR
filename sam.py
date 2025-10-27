def atm_withdrawal(balance,withdrawal):
    result =[]
    i=0
    while i<len(withdrawal):
        amount=withdrawal[i]
        if amount<=balance:
            balance-=amount
            result.append(f"withdrawn:{amount} rs")

        else:
            result.append(f"Balance is insufficient!!")
            result.append(f"You have {balance}")
            

        i+=1
    result.append(f"Remaining balance is:{balance}")
    return result


withdrawn =[383,59934,799,6899,8670,454]
balance = 10000

msg = atm_withdrawal(balance,withdrawn)
for msg in msg:
    print(msg)

