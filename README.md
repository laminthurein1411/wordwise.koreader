# wordwise.koreader

Rename wordwise.koreader.db to wordwise.db and replace from https://github.com/asxelot/wordwise.koplugin
If Kindle rewrite ./wordwise/wordwise.db from kll.en.en.klld. Need to delete that file and also replace wordwise.db

``python3 split_by_difficulty.py candidates.tsv``
This reads your TSV and writes difficulty_1.txt, difficulty_2.txt, etc. into the current directory (one word per line). For your example, difficulty_2.txt would contain just aah, and difficulty_1.txt would contain aardvark.

wordwise_en.db: 51735 entries
difficulty distribution (1 rarest .. 5 most common): {1: 38094, 2: 5503, 3: 4241, 4: 2746, 5: 1151}
