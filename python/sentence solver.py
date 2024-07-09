from itertools import permutations
from pathlib import Path

they = ['they'] * 3
do_not = ['don\'t'] * 2
know = ['know'] * 7
we = ['we'] * 4
that = ['that'] * 2

the_words = []
the_words.extend([*they, *do_not, *know, *we, *that])


for permutation in permutations(the_words):
    sentences = ' '.join(permutation)
    if not sentences.startswith('they they they'):
        print(sentences)

#
# location = Path(r'C:\Users\Admin\Desktop\permutations.txt')
#
# with open(location, 'w') as file:
#     file.write('')
