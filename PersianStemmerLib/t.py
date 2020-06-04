from persian_stemmer import PersianStemmer

ps = PersianStemmer()
while True:
    x = input()
    print(ps.run(x))