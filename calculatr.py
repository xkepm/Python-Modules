import mymath as mm

choose = input('Enter choice(1 for add / 2 for sub/3 for mul/4 for div): ')
if choose == '1':
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    mm.add(x,y)
elif choose == '2':
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    mm.sub(x,y)    
elif choose == '3':
    x = float(input('Enter first number:'))
    y = float(input('Enter second number:'))
    mm.mul(x,y)
elif choose == '4':
    x = float(input('enter firarst number:'))
    y = float(input('enter second number:'))        
    mm.div(x,y)
else:
    print("Invalid input")
