def readFile(file):
    
    f = open(file,"r",encoding="utf-8")
    str = f.read().split('\n')
    
    file1 = "newdecode.txt"
    f = open(file1,"w",encoding="utf-8")
    for item in str:
        f.write(f'{item},')
    return str

if __name__ == "__main__":
    stopwords =[]
    file1 = "Problem 1\\UAE.txt"
    stopwords = readFile(file1)
    print(stopwords)