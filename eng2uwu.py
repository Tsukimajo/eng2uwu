while True:
    words = input('Enter words here: ')
    x = words.replace('r', 'w').replace('l', 'w').replace('.', ". " + str(randchoice)).replace('k', 'cc')
    print(x)
    y = input('Would you like to enter something else? y/n ')
    print(y)
    if y == 'y':
        continue
    elif y == 'n':
        print('Goodbye')  
        break
    else:
        print('That is not a valid response. Goodbye')
        break