with open("count_the_words") as file:
   data = file.read().lower()

def unique_word_count(str):
    uniqueWords = dict()
    text = str.split()
    
    for word in text:
        if word in uniqueWords:
            uniqueWords[word]+=1
        else:
            uniqueWords[word]=1    
            
    return uniqueWords

output = sorted(unique_word_count(data).items())

print('Total number of unique words in the file is :', len(output))

for key, value in output:
   print(key.capitalize().ljust(15), ' ', value)
