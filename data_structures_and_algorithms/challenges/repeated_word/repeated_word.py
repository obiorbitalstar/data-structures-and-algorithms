import re
def repeated_word(string):
    to_lower_case = string.lower()
    word_list = re.findall('[\w\']+',to_lower_case)
    # print(word_list)
    repeat = {}
    for word in word_list:
        if word == ' ':
            continue
        elif word in repeat:
            if repeat[word] >= 1:
                return word
            else:
              repeat[word]+= 1
        else:
            repeat[word]=1



x = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
print(repeated_word(x))