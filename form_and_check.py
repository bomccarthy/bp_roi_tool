def check(number):
    if number == 'q':           # if 'q' is entered the program will exit
        exit()
    else:
        try:
            if number == '':          # if nothing is entered a zero will be returned
                return 0.0              # if somthing is entered a check for float will 
            else:                       # be returned or asked for re=entry recursively
                return float(number)
        except:
            check(input('This value must be a number without commas. Please re-enter the number or hit "q" to exit.  '))

def fmt(num):
    return "$ {:,.2f}".format(num)  # formats to a two decimal number with a '$'