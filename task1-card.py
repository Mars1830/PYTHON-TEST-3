def encrypt_card_number(card_number: str) -> str:
    card_number = card_number.replace(' ', '')
    encrypted_number = ''
    for i, symbol in enumerate(card_number):
        if i < 12:
            encrypted_number += '*'
        else:
            encrypted_number += symbol
    return encrypted_number


if __name__ == '__main__':
    print(encrypt_card_number('1234 5678 9123 4567'))