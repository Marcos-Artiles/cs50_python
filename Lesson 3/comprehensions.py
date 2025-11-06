#defining the main function
def main():

  #get the words from a text file
  words = get_words("address.text")

  #lowers the cose of the words if they are 4 letters long
  lowercase_words = [word.lower() for word in words if len(word) > 4]

  #building a dictionary with the count of times a word appeard in the words dictionary
  counts = {word: words.count(word) for word in lowercase_words}

  #counting the ammount of words
  for word in words:
    if word in counts:
      counts[word] += 1
    else
      counts[word] = 1

  save_counts(counts)

main()