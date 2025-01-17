# How to run
`python syllablelot.py`

You can go in the file and edit the starting word and how many words get generated.

# What is syllablelot?

This is a script that generates sequences of words with an interesting syllable structure. Specifically, consider that every word is composed of a sequence of syllables. For example, every word `Y` has a first syllable `Y_first` and a last syllable `Y_last`. For every word `Y` in the sentence, there is a relationship between that word `Y` and the word that is before it `X` and the word after it `Z`. Specifically, `Y_first == X_last` and `Y_last == Z_first`. For example:

```
['INCLUDE', 'DARK', 'CAUGHT', 'TONE', 'NUMBER', 'ORIGINAL', 'LEARN', 'NUMERAL', 'LEVEL', 'LONE', 'NOSE']
```