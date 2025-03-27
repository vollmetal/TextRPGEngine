


def handle_user_input(user_input_message: str, check_for_int: bool, check_input = '', error_message: str = ''):
        user_input = input(user_input_message)
        if check_for_int:
            if user_input.isdigit():
                if check_input is "":
                    return user_input
                else:
                    if user_input is check_input:
                        return user_input
                    else:
                        print(error_message)
            else:
                print(error_message)
        else:
            if check_input is "":
                    return user_input
            else:
                if user_input is check_input:
                    return user_input
                else:
                        print(error_message)