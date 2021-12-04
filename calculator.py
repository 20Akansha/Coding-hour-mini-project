Your_Choice = input('''Please select the type of operation you want to perform:
                     + for addition
                     - for subtraction
                     * for multiplication
                     / for division

                     ''')
 
First_num= int(input('Enter number: '))
Second_num= int(input('Enter number: '))
 
if Your_Choice == '+':
    print('{} + {} = '.format(First_num, Second_num))
    print(First_num + Second_num)
 
elif Your_Choice == '-':
    print('{} - {} = '.format(First_num, Second_num))
    print(First_num - Second_num)
 
elif Your_Choice == '*':
    print('{} * {} = '.format(First_num, Second_num))
    print(First_num * Second_num)
 
elif Your_Choice == '/':
    print('{} / {} = '.format(First_num, Second_num))
    print(First_num / Second_num)
 
else:
    print('''Please enter valid operator,
            try to run program again.''')
