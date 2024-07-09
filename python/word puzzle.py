import random
from collections import deque

sentence = 'maybe i should just be making longer sentences'

sentence_list = sentence.split(' ')


def word_randomise(word: str):
    word_list = deque(word)
    f_letter = word_list.popleft()
    l_letter = word_list.pop() if len(word) > 1 else []
    random.shuffle(word_list)

    new_word = ''.join(f_letter) + ''.join(word_list) + ''.join(l_letter)
    return new_word


new_sentence = [word_randomise(word) for word in sentence_list]
the_sentence: str = ' '.join(new_sentence)
print(the_sentence)
