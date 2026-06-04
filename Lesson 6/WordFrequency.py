# ### **Word Frequency Counter**
# **Objective**: Analyze a text file and count how often each word appears.  

# **Tasks**:  
# 1. **File Input**  
#    - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
#    - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

# 2. **Count Word Frequency**  
#    - Read the file content and split it into individual words.  
#    - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
#    - Ignore punctuation (like commas, periods, etc.).  

# 3. **Output**  
#    - Display the total number of words in the file.  
#    - Display the top 5 most common words with their counts.  
#    - Save the output to a new file called **"word_count_report.txt"**.  

# 4. **Example Output**  
#    **Content of sample.txt**:  
#        **Console Output**
# **Content of word_count_report.txt**:


with open("sample.txt", "r") as file:
    text = file.read()
    if not text:
        text = input("sample.txt is empty. Please enter a paragraph to create the file: ")
        with open("sample.txt", "w") as file:
            file.write(text)
import string
def count_word_frequency(text):
    word_count = {}
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
word_count = count_word_frequency(text)
total_words = sum(word_count.values())
print(f"Total number of words: {total_words}")
sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
top_5_words = sorted_word_count[:5]
print("Top 5 most common words:")
for word, count in top_5_words:
    print(f"{word}: {count}")
with open("word_count_report.txt", "w") as file:
    file.write(f"Total number of words: {total_words}\n")
    file.write("Top 5 most common words:\n")
    for word, count in top_5_words:
        file.write(f"{word}:{count}\n")
