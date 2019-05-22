def max_match(sentence, dictionary):
    # If sentence is empty, return an empty list
    if not sentence:
        return []
    #
    for i in range(len(sentence)-1, 0, -1):
        first_word = sentence[0:i+1]
        remainder = sentence[i+1:len(sentence)]
        if first_word in dictionary:
            return [first_word] + max_match(remainder, dictionary)
    first_word = sentence[0]
    remainder = sentence[1:]
    return [first_word] + max_match(remainder,dictionary)


dictionary_chinese = ['他', '特别', '喜欢', '北京烤鸭']
dictionary_english = ['we', 'can', 'canon', 'only', 'see', 'ash', 'a', 'short',
                      'ort', 'distance', 'stance', 'ahead', 'head']

print(max_match("他特别喜欢北京烤鸭", dictionary_chinese))
print(max_match("wecanonlyseeashortdistanceahead", dictionary_english))