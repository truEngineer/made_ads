STRING = None
LEN_STRING = 0
MAX_WORD_LEN = 0
NOT_TERMINAL = 0
 
 
class DictForest():
    
    def __init__(self):
        self.size = 1  # number of vertices
        self.n_words = 1  # number of words in foorest
        self.answers_words = []  # False - not in STRING, True - in STRING
        self.next_chr = {0: {}}  # dict: {vert number: dict: {char: next vert}}
        # problem with words ending with same chars!
        self.is_terminal = [NOT_TERMINAL]  # 0 - not terminal, word number - not
        
    def insert(self, word):
        # start_ind - index of the suffix first element
        # max_len - maximal word len
        len_word = len(word)
        vert_num = 0  # starting in root
        for ind in range(len_word):
            if word[ind] not in self.next_chr[vert_num]:
                self.next_chr[vert_num][word[ind]] = self.size
                self.is_terminal.append(NOT_TERMINAL)
                self.size += 1
            vert_num = self.next_chr[vert_num][word[ind]]
            if vert_num not in self.next_chr:
                    self.next_chr[vert_num] = {}
        self.is_terminal[vert_num] = self.n_words  # end of the word
        self.answers_words.append(False)
        self.n_words += 1
        
    def substring_contains(self, start_ind):
        vert_num = 0  # starting in root
        result = False
        for ind in range(start_ind, start_ind + MAX_WORD_LEN):  # words len is limited
            if ind > LEN_STRING - 1:
                break
            if not self.is_terminal[vert_num] == NOT_TERMINAL:  # if terminal
                ind_word = self.is_terminal[vert_num] - 1
                self.answers_words[ind_word] = True  # word is in STRING
                result = True
            if vert_num not in self.next_chr:  # achieve last vertice
                return result
            if STRING[ind] not in self.next_chr[vert_num]:  # no next char
                return result
            vert_num = self.next_chr[vert_num][STRING[ind]]
        if not self.is_terminal[vert_num] == NOT_TERMINAL:  # if terminal
            ind_word = self.is_terminal[vert_num] - 1
            self.answers_words[ind_word] = True  # word is in STRING
            result = True
        return result
 
 
STRING = input()
LEN_STRING = len(STRING)
n_words = int(input())
dictionary = DictForest()  # forest for words
for ind_word in range(n_words):
    new_word = input()
    dictionary.insert(new_word)
    len_word = len(new_word)
    if len_word <= LEN_STRING:
        if len_word > MAX_WORD_LEN:  # update max word len
            MAX_WORD_LEN = len_word
 
for ind_start in range(LEN_STRING):
    dictionary.substring_contains(ind_start)
result = ["Yes" if ans else "No" for ans in dictionary.answers_words]
print(*result, sep="\n")
