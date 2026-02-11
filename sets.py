#Program to count number of unique words in a given sentence using sets.
sentences=input("enter the sentence:")

words=sentences.split()
unique_word=set(words)
print(f"the unique words are:{unique_word}")
print(f"total number of unique word are:{len(unique_word)}")