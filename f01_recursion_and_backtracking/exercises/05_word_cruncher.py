def find_all_solutions(idx, target_text, word_index, words_count, used_words):
    if idx >= len(target_text):
        print(' '.join(used_words))
        return
    if idx not in word_index:
        return

    for word in word_index[idx]:
        if words_count[word] == 0:
            continue
        used_words.append(word)
        words_count[word] -= 1

        find_all_solutions(idx + len(word), target_text, word_index, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


text = input().split(', ')
target_text = input()
word_index = {}
words_count = {}

for word in text:
    if word in words_count:
        words_count[word] += 1
        continue
    else:
        words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target_text.index(word, idx)

            if idx not in word_index:
                word_index[idx] = []
            word_index[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

find_all_solutions(0, target_text, word_index, words_count, [])
