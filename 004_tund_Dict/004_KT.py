while True:
    try:
        isikukood=input('Enter ID code: ')
        int(isikukood)
        if len(isikukood)!=11:
            raise UserWarning
    except ValueError:
        print('Code you entered is not numeric!')
        continue
    except UserWarning:
        if len(isikukood)>11:
            print('too long code!')
        else:
            print('too short code!')
        continue
    else:
        print('ID CODE', isikukood)
        print(type(isikukood))

        while True:
            user_choice= input('Please choose:\n1.Print Gender\n2.Print date of birth\n3.Print Region\n4.Validate ID\n'
                               '5.Change ID\n0.Exit\n-->')
            if user_choice=='1':
                if int(isikukood[0])%2==0:
                    print('You are Female')
                else:
                    print('You are Male')

            if user_choice=='2':
                if isikukood[0] in'12':
                    bcent='18'
                elif isikukood[0] in '34':
                    bcent = '19'
                elif isikukood[0] in '56':
                    bcent = '20'
                elif isikukood[0] in '78':
                    bcent = '21'
                else:
                    print('Can\'t determinte date of birth')
                    continue
                print(f'Date of birth: {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}')

            if user_choice=='3':
                print(isikukood[7:10])
                if int(isikukood[7:10]) in range(1,11):
                   print('Region: Kuressaare haigla')
                elif int(isikukood[7:10]) in range(11, 20):
                    print('Region: Tartu Ülikooli Naistekliinik')
                elif int(isikukood[7:10]) in range(21, 151):
                    print('Region: Ida -Tallinna keskhaigla, Pelgulinna sünnitusmaja(Tallinn)')
                elif int(isikukood[7:10]) in range(151, 161):
                    print('Region: Keila haigla')

                elif int(isikukood[7:10]) in range(161, 221):
                    print('Region: Rapla haigla, Loksa haigla, Hiiumaa haigla(Kärdla)')
                elif int(isikukood[7:10]) in range(221, 271):
                    print('Region: Ida - Viru keskhaigla(Kohtla - Järve, endine Jõhvi)')
                elif int(isikukood[7:10]) in range(370, 372):
                    print('Region: Maarjamõisa kliinikum(Tartu), Jõgeva haigla')
                elif int(isikukood[7:10]) in range(420,422):
                    print('Region: Narva haigla')
                elif int(isikukood[7:10]) in range(421, 472):
                    print('Region: Pärnu haigla')
                elif int(isikukood[7:10]) in range(471, 491):
                    print('Region: Haapsalu haigla')
                elif int(isikukood[7:10]) in range(491, 521):
                    print('Region: Järvamaa haigla(Paide)')
                elif int(isikukood[7:10]) in range(521, 571):
                    print('Region: Rakvere haigla, Tapa haigla')
                elif int(isikukood[7:10]) in range(571, 601):
                    print('Region: Valga haigla')
                elif int(isikukood[7:10]) in range(601,651):
                    print('Region: Viljandi haigla')
                elif int(isikukood[7:10]) in range(651, 701):
                    print('Region Lõuna - Eesti haigla(Võru), Põlva haigla')
                else:
                    print('Väljaspool Eestit sündinud')

            if user_choice=='4':
                isikukood = list(map(int, isikukood))
                check1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
                check2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 0]
                check_list1 = [x * y for (x, y) in zip(isikukood, check1)]
                print(check_list1)
                check1_sum = sum(check_list1)
                print(check1_sum)
                control_num = (check1_sum - ((check1_sum // 11) * 11))
                print(control_num)
                if control_num == isikukood[10]:
                    print('Your code is valid')
                else:
                    check_list2 = [x * y for (x, y) in zip(isikukood, check2)]
                    check2_sum = sum(check_list2)
                    control_num = (check2_sum - ((check2_sum // 11) * 11))
                    print(control_num)
                    if control_num == isikukood[10]:
                        print('Your code is valid')
                    else:
                        print('You are LIER!')

            if user_choice == '5':
                break

            if user_choice=='0':
                print('Good bay!')
                quit()

    #else:
        #print('Your choice is out of range')

