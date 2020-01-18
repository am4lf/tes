import re 

def wordsCount(sentence):
    if type(sentence) == int:
        return "Parameter harus string"
    else:
        words = sentence.split()
        #cek word
        listword = []
        for word in words:
            cek = isWord(word)
            if cek == True:
                listword.append(word)
        wordCount = len(listword)
        return str(wordCount)+'/'+str(len(words))
        
def isWord(word):
    if re.match(r'[A-Za-z]', word):
        return True
    else:
        return False

print(wordsCount("Ini adalah 56 kata !!!"))