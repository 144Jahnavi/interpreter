def word_count(sentence):
    sentence = sentence.lower()
    result = {}
    punct = ".,!?;:'\"()-[]{}"

    for word in sentence.split():
        for p in punct:
            word = word.replace(p, '')   
        if word:
            result[word] = result.get(word, 0) + 1
    return result


print(word_count("Hello, hello! How are you? You look well."))
