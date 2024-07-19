def alpha_numerical(password):
    password = password.lower()
    checker = {'numericals' : False, 'alphabets' : False}
    for string in password:
        if string.isdigit():
            password = password.replace(string, '')
            checker['numericals'] = True
        else:
            checker = checker

    if password.isalnum() == True:
        checker['alphabets'] =  True
        return checker['alphabets']  and checker['numericals']
    else:
        return False

print(alpha_numerical('P4ssW0rD'))