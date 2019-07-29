
def plural(word):
    if(word[-3:]== "ife"):
        return  word[:1] + "ives"
    elif(word[-2:] == "sh"):
        return word[:-2] +"shes"
    elif(word[-2:] == "us"):
        return word[:4] + "i"
    elif(word[-2:] == "sh") or (word[-2:] == "ch"):
        return word + "es"

    else: return word + 's'
w = raw_input("Pluralize the word: ")
print plural(w)
x = raw_input("Would you like to repeat: Y/N ")

while(x == "Y"):
    w = raw_input("Pluralize the word: ")
    print plural(w)
    x = raw_input("Would you like to repeat: Y/N")
    if(x =="Y"):
        continue
    elif x == "N":
        break
    else:
        raw_input("Invalid Response. Use Y/N: ")
        continue
