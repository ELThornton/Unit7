# Elena Thornton
# 11/14/2017
# Unit_7.py


def alphabet_shift(alphabet):
    """
    this shifts the alphabet over.
    :param alphabet:is the alphabet
    :return:shift
    """

    user_shift = int(input("how many spots do you want to shift the alphabet if a is 0:",))
    part_one = alphabet[user_shift:]
    part_two = alphabet[:user_shift]
    shift = part_one + part_two

    return shift


def message(alphabet, shifted):
    """
    this shifts the message
    :param alphabet:original alphabet
    :param shifted:shifted alphabet
    :return:new_message
    """
    user_message = input("what do you want you  message to be:",)
    new_message = ""
    for character in user_message:
        a = alphabet.index(character)
        b = shifted[a]
        new_message = new_message + b
    print("this is your new message", new_message)
    return new_message


def decode_message(alphabet, new, shifted):
    """
    this decodes the message
    :param alphabet:original alphabet
    :param new:this is the new message
    :param shifted:shifted alphabet
    :return:nothing
    """
    yes_or_no = input("would you like to decode your message?(yes or no):",)
    if yes_or_no == "yes":
        decoded_message = ""
        for character in new:
            a = shifted.index(character)
            b = alphabet[a]
            decoded_message = decoded_message + b
        print("you decoded message is", decoded_message)
    elif yes_or_no == "no":
        print("that's for using this program.")


def main():

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted = alphabet_shift(alphabet)
    print(shifted)
    new = message(alphabet, shifted)
    decode_message(alphabet, new, shifted)


main()
