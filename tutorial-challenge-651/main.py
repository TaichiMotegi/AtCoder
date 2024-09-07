
def main(s):
    symbol = {"@", "$", "%"}

    for i in range(5, len(s)):
        for j in range(len(s)):
            if i + j > len(s) - 1:
                break
            word = s[j:i+j+1]
            if "@" in word or "$" in word or "%" in word:
                word_set = set(word)
                word_set = word_set - symbol
                if len(word_set) >= 5:
                    print(i+1)
                    exit()
    print(len(s))

if __name__ == '__main__':
    s = input()
    main(s)