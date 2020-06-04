from PersianStemmerLib import PersianStemmer

#used https://github.com/htaghizadeh/PersianStemmer-Python/tree/master/PersianStemmer with some changes
def stem_list(words_list):
    ps = PersianStemmer()
    for i in range(len(words_list)):
        words_list[i] = ps.run(words_list[i])
    return words_list