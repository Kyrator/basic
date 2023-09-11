# TODO здесь писать код

word = input("Введите слово: ")
count_case = 0
count_word = len(word)
for i in range(count_word // 2):
    if word[i] == word[count_word - i - 1]:
        count_case += 1
        if count_case == count_word // 2:
            print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")
        break
