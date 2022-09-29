while True:
    try:
        user_input=input('Enter ID code: ')
        int(user_input)
        if len(user_input)!=11:
            raise UserWarning
    except ValueError:
        print('Code you entered is not numeric!')
        continue
    except UserWarning:
        if len(user_input)>11:
            print('too long code!')
        else:
            print('too short code!')
        continue
    else:
        print('ID CODE', user_input)
        break
#ValueError: