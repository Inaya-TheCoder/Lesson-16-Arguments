def total_calc(bill_amount,tip_per):
    total = bill_amount*(1 + 0.01 * tip_per)
    total =round (total,2)
    print (f"Please Pay $",total)
total_calc(300,80)