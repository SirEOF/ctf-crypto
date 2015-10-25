__author__ = 'Chris Iler'

def get_bigrams(text):
    out = {}
    temp = {}
    text = text.lower()
    text = text.replace(" ", "")
    for i in range(len(text)-1):
        bigram = text[i:i+2]
        if bigram in temp:
            temp[bigram] += 1
        else:
            temp[bigram] = 1
    for key in temp:
        if not temp[key] == 1:
            out[key] = temp[key]
    import operator
    return sorted(out.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    print(get_bigrams("the quick brown fox jumped over the lazy dogth"))