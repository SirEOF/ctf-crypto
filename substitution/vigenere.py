__author__ = 'Chris Iler'


def get_bigrams(text):
    out = {}
    temp = {}
    text = text.lower()
    text = text.replace(" ", "")
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        if bigram in temp:
            temp[bigram] += 1
        else:
            temp[bigram] = 1
    for key in temp:
        if not temp[key] == 1:
            out[key] = temp[key]
    import operator
    return sorted(out.items(), key=operator.itemgetter(1), reverse=True)



def encrypt(text, key):
    out = ""
    text = text.lower()
    text = text.replace(" ", "")
    key = key.lower()
    key = key.replace(" ", "")
    for i in range(0, len(text) - 1):
        out += chr((((ord(text[i]) + ord(key[i % len(key)])) - 0xC2) % 26) + 0x61)
    return out



def brute_force(text, keyLength, thresh):
    import analysis
    key = ""
    for i in range(keyLength):
        key += "a"
    notDone = True
    while notDone:
        temp = encrypt(text, key)
        if analysis.englishRank(temp) > thresh:
            print(temp + " " + key + " " + str(analysis.englishRank(temp)))
        out = increment_key(key)
        key = out[0]
        notDone = out[1]



def increment_key(key):
    keyl = list(key)
    for i in range(len(keyl)):
        if keyl[i] == "z":
            keyl[i] = "a"
        else:
            keyl[i] = chr(ord(keyl[i]) + 1)
            return (''.join(keyl), True)
    return (''.join(keyl), False)



if __name__ == '__main__':
    print(encrypt("abcdef", "ghijk"))
    #print(get_bigrams("the quick brown fox jumped over the lazy dogth"))
    brute_force("Dnsqcmwq odlnzs xa tzq dn ytq bwxf mcknqzi ntdyh wk odnxyasgiutk Xv ytq bwxf exuuxq Kqlqztzj ouepjd ytaxmsta fdq tvhdkebjp nn iihmcknzs tiht xtbyqd dvj eftx Kad tffybam F nqrwrqe Q J gqoduje O tbh mzs H gqoduje M Iw iqogguf m Kqlqztzjqzrwiqp bmxemvm ytq eztoqha ne exuuxk gmaqdhmi",5, 0.1)
