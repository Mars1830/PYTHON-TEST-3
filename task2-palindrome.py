def is_palindrome(word: str) -> bool:
    word = word.replace(' ', '')
    length = len(word)
    half_length = length // 2
    if length % 2 == 1:
        return word[:half_length] == word[: half_length:-1]
    else:
        return word[:half_length] == word[: half_length - 1:-1]


if __name__ == '__main__':
    print(is_palindrome('abba'))
    print(is_palindrome('level'))
    print(is_palindrome('qwertyu'))
    print(is_palindrome('was it a cat i saw'))
