import random

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def get_words(text):
    symbols = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '"', "'", '\n', '\r']
    for s in symbols:
        text = text.replace(s, ' ')
    
    raw_words = text.split()
    words = []
    for w in raw_words:
        if any(c.isalpha() for c in w):
            words.append(w)
    return words

def make_chain(words, chain_length):
    chain = {}
    for i in range(len(words) - chain_length):
        if chain_length == 2:
            key = (words[i], words[i+1])
        elif chain_length == 3:
            key = (words[i], words[i+1], words[i+2])
        else:
            key = (words[i],)
            
        next_word = words[i + chain_length]
        
        if key not in chain:
            chain[key] = []
        chain[key].append(next_word)
        
    return chain

def generate_text(chain, words, chain_length, output_len):
    start_word = None
    for w in words:
        if w[0].isupper():
            start_word = w
            break
            
    if start_word is None:
        return "Не найдено слов с заглавной буквы."

    result_words = []
    if chain_length == 2:
        for i in range(len(words) - 1):
            if words[i] == start_word:
                result_words = [words[i], words[i+1]]
                break
    elif chain_length == 3:
        for i in range(len(words) - 2):
            if words[i] == start_word:
                result_words = [words[i], words[i+1], words[i+2]]
                break
    else:
        result_words = [start_word]

    current_len = len(result_words)
    
    while current_len < output_len:
        if chain_length == 2:
            key = (result_words[-2], result_words[-1])
        elif chain_length == 3:
            key = (result_words[-3], result_words[-2], result_words[-1])
        else:
            key = (result_words[-1],)
            
        if key not in chain:
            break
            
        possible_words = chain[key]
        next_w = random.choice(possible_words)
        
        result_words.append(next_w)
        current_len += 1

    return ' '.join(result_words)

filename = input("Введите имя файла (например, Книга.txt): ")
length = int(input("Введите длину текста в словах: "))

text = read_file(filename)
words = get_words(text)

print("\nЦепочка по 2 слова")
chain_2 = make_chain(words, 2)
print(generate_text(chain_2, words, 2, length))

print("\nЦепочка по 3 слова")
chain_3 = make_chain(words, 3)
print(generate_text(chain_3, words, 3, length))