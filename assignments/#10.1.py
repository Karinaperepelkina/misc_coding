
#10.1 Split large number into hundreds, tens and units.


print('This program split given large number into hundreds, tens and units.')


num = float(raw_input('Enter a number: '))

i = 10
while num > 0:
        c = num % i
        num = num - c
        i = i*10
        print(c)

              
