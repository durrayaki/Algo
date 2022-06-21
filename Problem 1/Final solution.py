import pandas as pd 
import re

#read txt file and convert to array
def readFile(file,array):
    f = open(file,"r",encoding="utf-8")
    array = f.read().split(',')
    return array

def countPositive(pairlist,positive,country):
    totalPositive = 0 
    pairPositive = []
    
    #string matching
    for i in pairlist:
        for j in positive:
            if i[0] == j:
                #print(j +","+str(i[1]))
                pairPositive.append([i[0],i[1]])
                totalPositive = totalPositive + i[1]
            else:
                continue
            
    #print("Total Positive words for country ["+country+"] = " +str(totalPositive)) 
    df = pd.DataFrame(pairPositive)
    df['pos_total'] = pd.Series(totalPositive, index=df.index[[0]])
    df.columns = ['pos_word', 'pos_freq','pos_total']
    df.to_csv("Problem 1\CSV Files\\"+country + ' positive.csv',index=False)             
    return totalPositive

def countNegative(pairlist,negative,country):
    totalNegative = 0
    pairNegative = []
    for i in pairlist:
        for j in negative:
            if i[0] == j:
                #print(j +","+str(i[1]))
                pairNegative.append([i[0],i[1]])
                totalNegative = totalNegative + i[1]
            else:
                continue
    #print("Total Negative words for country ["+country+"] = " +str(totalNegative)+"\n\n") 
    df = pd.DataFrame(pairNegative)
    df['neg_total'] = pd.Series(totalNegative, index=df.index[[0]])
    df.columns = ['neg_word', 'neg_freq', 'neg_total'] 
    df.to_csv("Problem 1\CSV Files\\"+country + ' negative.csv',index=False)        
    return totalNegative

def countwordfreq(file):
    #read the article
    f = open(file,"r",encoding="utf-8") 
    article = f.readline()
    f.close()

    #split the words using various delimiter
    wordlist = re.split(';|,|\*|\n| |\|.|[|]|/|:|!',article)
    wordfreq = [] #initialize empty array for word frequency
    pairlist = [] #initialize empty array for pair list 

    #count the frequency of the word
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    #[(word,frequency),...]
    pairlist = list(dict.fromkeys(zip(wordlist, wordfreq)))
    return pairlist

def filterStopWords(pairlist,stop,country):
    for i in pairlist:
        for j in stop:
            if i[0] == j:
                pairlist.remove(i)
            else:
                continue
    return pairlist

def ranking(pairlist,positive,negative,country,rank):
    totalPositive = countPositive(pairlist,positive,country)
    totalNegative = countNegative(pairlist,negative,country)
    socialRank = float("{:.2f}".format((totalPositive - totalNegative)/(totalPositive + totalNegative)*100))
    rank.append([country,totalPositive,totalNegative,socialRank])
    return rank

def sortRanks(rank):
    rank.sort(key=takeSecond, reverse=True)
    print("====================================\tSocial Rank\t====================================")
    df = pd.DataFrame(rank)
    #df['neg_total'] = pd.Series(rank, index=df.index[[0]])
    df.columns = ['Country','Total Positive','Total Negative', 'Diff. Percentage[%]']
    df.index = df.index + 1
    
    print(df)

# take second element for sort
def takeSecond(elem):
    return elem[1]
   
#driver code    
if __name__ == "__main__":
    #initialize empty array for positive,negative and stop words
    country = ["Canada","China","Phillipines","Singapore","UAE"]
    positive = []
    negative = []
    stop = []

    #read txt file to fill in the arrays of positive,negative and stop words 
    file1 = "Problem 1\Article\\positive.txt"
    positive = readFile(file1,positive)
    file2 = "Problem 1\Article\\negative.txt"
    negative = readFile(file2,negative)
    file3 = "Problem 1\Article\stopwords.txt"
    stop = readFile(file3,stop)
    
    rank = []
    for article in country:
        file = "Problem 1\Article\\" + article + ".txt"
        #print("=========================================\t"+article+"\t=========================================")
        pairlist = countwordfreq(file)
        filterStopWords(pairlist,stop,file)
        ranking(pairlist,positive,negative,article,rank)
     
    sortRanks(rank)   
    