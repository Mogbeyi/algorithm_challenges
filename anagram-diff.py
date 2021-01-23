def difference(first_word, second_word):
    if len(first_word) != len(second_word):
        return -1

    def build_dic(word):
        hash_table = {}

        for letter in word:
            if letter in hash_table:
                hash_table[letter] += 1
            else:
                hash_table[letter] = 1

        return hash_table

    first_word_table = build_dic(first_word)
    second_word_table = build_dic(second_word)
    count = 0

    for key in first_word_table.keys():
        if key in second_word_table:
            count += abs(first_word_table[key] - second_word_table[key])
        else:
            count += first_word_table[key]

    return count

print(difference('toe', 'tie'))
print(difference('faang', 'beemg'))
print(difference('hello', 'hell'))
print(difference('love', 'life'))
