punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

def get_pos(sentence):
    sentence = sentence.lower()
    sentence = sentence.split()
    positive_count = 0
    for word in sentence:
        word = strip_punctuation(word)
        if word in positive_words:
            positive_count += 1
    return positive_count

def get_neg(sentence):
    sentence = sentence.lower()
    sentence = sentence.split()
    negative_count = 0
    for word in sentence:
        word = strip_punctuation(word)
        if word in negative_words:
            negative_count += 1
    return negative_count

# Open the input and output files
input_file = open("project_twitter_data.csv", "r")
output_file = open("resulting_data.csv", "w")

# Write headers to the output file
output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
output_file.write("\n")

# Read each line of the input file and calculate the sentiment scores
lines = input_file.readlines()
for line in lines[1:]:
    fields = line.strip().split(",")
    retweets = fields[1]
    replies = fields[2]
    positive_score = get_pos(fields[0])
    negative_score = get_neg(fields[0])
    net_score = positive_score - negative_score
    # Write the sentiment scores to the output file
    output_file.write("{}, {}, {}, {}, {}".format(retweets, replies, positive_score, negative_score, net_score))
    output_file.write("\n")

# Close the input and output files
input_file.close()
output_file.close()
