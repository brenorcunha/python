records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3,4),
]
def do_foo(x,y):
    print('foo', x, y)
def do_bar(s):
    print('bar',s)
for tag, *args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)
        
#var = input('Do you want to contract extra shipping? (yes/not) \n')
# This prevents using var = 'yes' or var='YES' or var = 'Yes', etc...
#if var.lower() == 'yes':
#    print('OK, the price will be normal price + $10. ')
#else:
#    print('Please, help us, we are poor! A litlle money please... ')

#if answer='yes'
#if not answer='no'

#if float(total) < 100
#if not total >= 100 IT BUGGED MY MIND
#deposit = input('How much do you want to deposit now? ')
#if float(deposit) > 100:
#    print('Congratulations. You won a toaster. Enjoy it! ')
#else:
#    print('You won a mug!')
#print('Dankewel mensen! Tot ziens!')

#opt1 = input('Do you won a lottery prize? (y/n)\n')
#if (opt1).lower() == 'y':
#    wonLottery = True
#else:
#    wonLottery = False
#opt2 = input('A big prize was warned in lottery? (y/n) \n')
#if (opt2).lower() == 'y':
#    bigWin = True
#else:
#    bigWin = False
    
#if wonLottery == False and bigWin == False:
#    print('Oh! that\'s too bad... ')
#elif wonLottery and bigWin ==False:
#    print('Oh! that\'s too bad... ')
#elif wonLottery == False and bigWin:
#    print('Oh! that\'s too bad... ')
#elif wonLottery and bigWin:
#    print('Congratulations! Not work anymore in your life!!!')
#else:
#    print('Well... If you\'re seeing this message, something wrong is not right...')