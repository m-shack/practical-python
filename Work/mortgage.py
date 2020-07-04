# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_number = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if (payment_number+1 >= extra_payment_start_month and payment_number+1 <= extra_payment_end_month):
        extra_amount = extra_payment
    else:
        extra_amount = 0
    if (principal * (1+rate/12)) < (payment + extra_amount):
        payment = principal * (1+rate/12)
        extra_amount = 0
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment - extra_amount
    total_paid = total_paid + payment + extra_amount
    payment_number += 1
    print(payment_number, total_paid, principal)

print(f'Total paid: {total_paid:.2f} over {payment_number} months.')