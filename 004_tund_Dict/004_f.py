try:
    user_input = float(input('Enter float: ')) #check conditions for errors
except:         #for mistake
    print('You entered not float.')
else: # if correst
    print(user_input)
finally: #will in any case
    print('Good bay!')
#ValueError: