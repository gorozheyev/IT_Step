unique_words = []

with open("simple.txt", 'r') as myfile:
    count = 0
    text = myfile.read()
    list_of_words = text.replace(",", "").replace(".", "").replace(":", "").replace("!", "").replace("?", "").lower().split()
    print("количество слов в файле: ", len(list_of_words))

    for i in list_of_words:
        if i not in unique_words:
            unique_words.append(i)
            count += 1
    print(f"количество уникальных слов в файле: {count}")

    new_count = 0
    for j in unique_words:
        for k in list_of_words:
            if j == k:
                new_count = new_count +1
        print(f"{j} - {new_count} раз" )
        new_count = 0
