import module_exit
def menu():
    print ('\n1.Create')
    print ('2.Contact')
    print ('3.Find')
    print ('4.Edit contact')
    print ('5.Delete')
    print ('6.Exit')

    selection=int(input('\nChoose the number '))

    if selection == 1:
        print ('Not Exist')
    elif selection == 2:
        print ('Not Exist')
    elif selection == 3:
        print ('Not Exist')
    elif selection == 4:
        print ('Not Exist')
    elif selection == 5:
        print ('Not Exist')
    elif selection == 6:
        module_exit.exit()

    else:
        print('Not Exist')

    menu()
    selection = int(input("Choose: "))

menu()

