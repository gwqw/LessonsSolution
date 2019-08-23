def is_palindrom(str):
    return str == str[::-1]

def longest_palindromic(text):
    print("text: ", text, " with len: ", len(text))
    max_pal_length = 0
    max_pal = text
    for b in range(len(text)-1):
        for e in range(b+1, len(text)+1):
            test_str = text[b:e]
            print(f"test_str: {test_str} from {b} to {e}")
            if is_palindrom(test_str) and e-b>max_pal_length:
                max_pal_length = e-b
                max_pal = test_str
    print(f"Max pal for {text} is {max_pal} with length {max_pal_length}")
    return max_pal

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("1") == "1", "1"
