import random

def load_syllables(path : str = "./syllables.txt") -> dict[str,list[str]]:
    f = open(path,"r")
    contents = f.readlines()

    world2syllable = {}

    for l in contents:
        if ";" not in l:
            d = l.split(" ")
            d[-1] = d[-1][:-1]
            world2syllable[d[0]] = d[2:]

    return(world2syllable)

def load_common_words(path : str = "./1000-most-common-words.txt"):
     # Open the file in read mode
    with open(path, 'r') as file:
        # Read lines into a list
        common_words = file.readlines()
    common_words = [line.strip().upper() for line in common_words]
    return(common_words)

def syllable_slam(syllable_list1 : list[str],syllable_list2 : list[str]) -> bool:
     
	return syllable_list1[-1] == syllable_list2[0]


def generate_slammable_words(word : str, world2syllable : dict[str,list[str]]) -> list[str]:
	#words that follow from it
	words = []
	for w in world2syllable.keys():
		if syllable_slam(world2syllable[word],world2syllable[w]):
			words.append(w)
	return words

def make_fun_sequence(fword : str, world2syllable : dict[str,list[str]], common_words : list[str], num_words : int = 10) -> list[str]:
     sentence = [fword]
     for _ in range(num_words):
        try:
            rhyme_words = generate_slammable_words(sentence[-1], world2syllable)
            useful_words = [a_word for a_word in rhyme_words if a_word in common_words ]
            next_word = random.choice(useful_words)
            sentence.append(next_word)
        except IndexError:
             break
     return(sentence)

if __name__ == "__main__":
     words2syllables = load_syllables()
     common_words = load_common_words()

     starting_word = random.choice(common_words)
     max_num_words_in_sentence = 100

     fun_sentence = make_fun_sequence(starting_word, words2syllables,common_words,max_num_words_in_sentence)
     print(fun_sentence)