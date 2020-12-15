phrase = input("Введите фразу: ")
phrase_list = (phrase.split())
max_char = 10
a = 1
for i in phrase_list:
    print(a, i[0:max_char], end="\n")
    a+=1

