amount = int(input('what is the amount?:'))
vat = int(input('wat is the vat percentage?:'))
new_vat = vat / 100
p = amount * new_vat
payment = amount + p
print ('the total payment is:', payment)