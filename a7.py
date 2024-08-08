total=0
while True:
    deposite_withdraw_tran=input()
    if deposite_withdraw_tran =="":
        break
    else:
        deposite_withdraw_tran = deposite_withdraw_tran.split(" ")
        if deposite_withdraw_tran[0] =="d":
            total = total + int(deposite_withdraw_tran[1])
        elif deposite_withdraw_tran[0] =="w":
            total = total - int(deposite_withdraw_tran[1])
print(total)                