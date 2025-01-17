# Syllablelot

## How to Run
To run the script, use the following command:

```bash
python syllablelot.py
```

You can modify the starting word and the number of words generated by editing the `syllablelot.py` file directly at the bottom. By default, it chooses a random common word as the starting word.

## What is Syllablelot?
Syllablelot is a Python script that generates sequences of words with a unique syllable structure. The words in the sequence are connected through their syllables. Specifically, every word `Y` in the sequence has a first syllable `Y_first` and a last syllable `Y_last`. The relationship between consecutive words `X`, `Y`, and `Z` is as follows:

- `Y_first` matches `X_last`
- `Y_last` matches `Z_first`

### Example
```
['PLACE', 'SKIN', 'NOR', 'REMEMBER']
```
In this example:
- `PLACE_last` matches `SKIN_first`
- `SKIN_last` matches `NOR_first`
- `NOR_last` matches `REMEMBER_first`

This structure creates an interesting chain of words based on syllabic continuity.

