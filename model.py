from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('data/slogans.txt', num_epochs=60)