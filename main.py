#1. Read the entire of "Dracula" usinf the function below:
# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

#load the book
draculaText = readBook()

#2. Display the word that shows up the MOST often

# Convert the text into a list of words. split() function convert a string to a list of words.
words = draculaText.split()
count = 0
# Create a dictionary to count how many times the word shows up
wordCount = {}
# Go through each word...
for word in words:
# Account for capitalization differences
  
   if word.lower() == "a":
      count += 1
 
  # Is it already in the dictionary?
if word in wordCount:
    
    # If so, increment it's count
    wordCount[word] +=1
  # If not, create the pair and set it's initial count to 1
else:
    print(f"{word} - {wordCount}")

# Display the word that shows up the most and the word with the most characters
for key, value in wordCount:
  print({key},{value})
  print(len(word))

  
  # Does the current word show up more times than the current king?
    
    # Save the word as the current "king"

    # Save the number of times it appears as the current "rank"

  # Is this a four letter word?

# Display the most frequently used word (usually "the")

# Display the longest word that was found

# Display all words that appear more than 500 times





























# create a dictionary
from statistics import mode
mode = mode(draculaText)
dict = {}

for key in dict:
  if key > mode(draculaText):
    key == mode(draculaText)

else:
  print("That state and capital are already in the dictionary.")















def most_often():
    count = 0
    num = ""

    for i in List:
      current_frequency = List.count(i)
      #if current_frequency > count:
      count = current_frequency
      
    return num
    
List = readBook()
#print(most_often(List))






#3. How many UNIQUE four-letter words are in the book?
darculaText = readBook()

count = 0
words = darculaText.split()

for word in words:
  if len(word)== 4:
    count = count + 1
  print(count)
    
  
#4. Display every word that shows up MORE THAN 500 times

for word in words:
   
  if count(word)> 500:
    
    print(word)

#5. How many times that word (in (#4.) shows up throughout the book?

list = []

appearnace = 0

for word in words:
  if count(word) > 500:
    appearance = appearnace + 1
    print(appearance)

