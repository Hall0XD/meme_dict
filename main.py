meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
    # Что делать, если слово нашлось?
        print(meme_dict[word])
    else:
        print(word,'это ты')
