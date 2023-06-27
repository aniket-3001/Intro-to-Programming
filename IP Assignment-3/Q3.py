import random


def compute_F1(words, tot_words):
    tot_unique_words = len(set(words))
    return tot_unique_words / tot_words


def compute_F2(word_freq, tot_words):
    top_5_occ = 0
    for i in range(5):
        if i < len(word_freq):
            top_5_occ += word_freq[i][1]
    return top_5_occ / tot_words


def compute_F3(sentences):
    long_short_sentences = 0
    for sentence in sentences:
        if len(sentence.split()) > 35 or len(sentence.split()) < 5:
            long_short_sentences += 1
    return long_short_sentences / len(sentences)


def compute_F4(contents, tot_words):
    consec_punc_marks = 0
    for i in range(len(contents) - 1):
        if contents[i] in '.?,!':
            if contents[i] == contents[i+1]:
                consec_punc_marks += 1
    return consec_punc_marks / tot_words


def compute_F5(tot_words):
    return 1 if tot_words > 750 else 0


# list of input file names
IP_files = ['D:/Aniket/PYTHON_CODES/IP Assignment-3/file1.txt', 'D:/Aniket/PYTHON_CODES/IP Assignment-3/file2.txt',
            'D:/Aniket/PYTHON_CODES/IP Assignment-3/file3.txt', 'D:/Aniket/PYTHON_CODES/IP Assignment-3/file4.txt', 'D:/Aniket/PYTHON_CODES/IP Assignment-3/file5.txt']
for IP_file in IP_files:
    # read the contents of the file and store into a string
    with open(IP_file, "r", encoding="utf-8") as f:
        contents = f.read()

    contents = "".join(c.lower() for c in contents if c.isalpha() or c in [
        ' ', '\n', '.', '?', '!', ',', ';', ':'])

    # split the content into words
    words = [c.strip(",.?!;:") for c in ((contents.strip()).split())]

    # count the total number of words
    tot_words = len(words)

    # count the occurrences of each word and storing in a dictionary
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq[word] + 1 if word in word_freq else 1

    # sort the word count dictionary by value
    word_freq = sorted(
        word_freq.items(), key=lambda x: x[1], reverse=True)

    # split the contents into sentences
    sentences = contents.split('. ')

    # calculate the factors
    F1 = compute_F1(words, tot_words)
    F2 = compute_F2(word_freq, tot_words)
    F3 = compute_F3(sentences)
    F4 = compute_F4(contents, tot_words)
    F5 = compute_F5(tot_words)

    # calculate the final score
    score = 4 + F1 * 6 + F2 * 6 - F3 - F4 - F5

    # append the results to file score.txt
    with open('scores.txt', 'a') as f:
        f.write(IP_file + '\n')
        f.write(f"score: {score}\n")
        f.write('top 5 words: ')
        for i in range(5):
            if i < len(word_freq):
                f.write(f"{word_freq[i][0]}, ")
        f.write('\n')
        f.write('random words: ')
        for i in range(5):
            random_index = random.randint(0, len(words) - 1)
            f.write(f"{words[random_index]}, ")
        f.write('\n\n')
    print(f"data appended successfully for {IP_file}")
