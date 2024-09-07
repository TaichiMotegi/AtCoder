from itertools import permutations


def main():

    s = input()
    # 入力された値をソート
    s_sorted = sorted(s)
    # 重複をなくすためのsetを用意
    words = set()
    # 文字の順列を列挙
    for char in permutations(s_sorted):
        word = "".join(char)
        # set二格納することで文字列の重複を無くす
        words.add(word)
        # 入力された値と同じ値だった場合ループを抜ける
        if word == s:
            break
    # 事前にソートされているためsetの長さが答えとなる
    print(len(words))


if __name__ == "__main__":
    main()
