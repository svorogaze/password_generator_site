import secrets

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'y', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'Y', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['$', '?', '!', '@', '#', '%']


def generate_password(bool_lowercase, bool_uppercase, bool_nums, bool_spec_chrs, len_of_password):
    password = ''

    chars = []
    if bool_lowercase:
        chars += lowercase_letters
    if bool_uppercase:
        chars += uppercase_letters
    if bool_nums:
        chars += nums
    if bool_spec_chrs:
        chars += special_chars

    for i in range(len_of_password):
        password += secrets.choice(chars)

    return password


if __name__ == '__main__':
    print(generate_password(True, True, True, True, 16))
