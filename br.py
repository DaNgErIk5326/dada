def check_password(pasword):
    correct_password = "dB7nQ!oV"
    if password == correct_password:
        return True
    return False

def brute_force(password_list):
    for password in password_list:
        if check_password(password):
            print("ACCESS GRANTED! Password is {password}")
            return password
    print("пароль не знайдений.")
    return None

passwords