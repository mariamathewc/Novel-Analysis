from collections import Counter
import re
f = open("C:\\Users\maria\Documents\Desktop\lwmen10.txt", "r")
fc = open("C:\\Users\maria\Documents\Desktop\common100.txt", "r")

characters_to_remove = '!().:;,\"'
pattern = "[" + characters_to_remove + "]"


# Finds total no of words in file
def TotalNumberOfWords():
    num_words = 0
    new_string = re.sub(pattern, "", f.read())
    words = new_string.split()
    num_words += len(words)
    return num_words

word_count = TotalNumberOfWords()
print("Number of words: ", word_count)

dicts={}
mylist=[]


# Finds total unique words in file
def getTotalUniqueWords():
    f.seek(0, 0)
    new_string = re.sub(pattern, "", f.read())
    words = new_string.split()
    
    for wrd in words:
        mylist.append(wrd)
        #print(wrd)
        dicts[wrd] =dicts.get(wrd,0)+1
            
    return len(dicts)

unq_wrd = getTotalUniqueWords()
print("Number of unique words: ", unq_wrd)


# Finds 20 most frequent word in file
def get20MostFrequentWords():
    f.seek(0, 0)
    word_counts = Counter(mylist)
    top_20 = word_counts.most_common(20)
    print("20 most frequent words are: ",top_20)
    
get20MostFrequentWords()


# Find 20 most interesting words in file
comm_list =[]
for line in fc:
    words = line.split()
    for wrd in words:    
        comm_list.append(wrd)
        
def get20MostInterestingFrequentWords():
    ans =[]
    for k, v in sorted(dicts.items(), key=lambda item: item[1], reverse=True):
        if k not in comm_list:
            ans.append([k,dicts.get(k)])
        if len(ans)==20:
            break
    print("20 most interesting words are: ",ans)
    
get20MostInterestingFrequentWords()


# Finds 20 least frequent word in file
def get20LeastFrequentWords():
    ans = []
    for k, v in sorted(dicts.items(), key=lambda x:x[1]):
        ans.append([k,v])
        if len(ans)==20:
            break
    print("20 least frequent words are: ",ans)
    
get20LeastFrequentWords()


# Find frequency of a word in each chapter
def getFrequencyOfWord(word):
    f.seek(0, 0)
    ans =[]
    #i =0
    count=0
    for line in f:
        words = line.split()
        for wrd in words:
            if wrd == "CHAPTER":
                #ans[i]=count
                ans.append(count)
                count =0
                #i+=1
            elif wrd == word:
                count+=1
    #ans[i]=count
    ans.append(count)
    ans.pop(0)
    print("Frequency of word in each chapter: ",ans)
    
word ="death"
getFrequencyOfWord(word) 


# Find the chapter no to which a quote belongs
def getChapterQuoteAppears(searchQuote):
    f.seek(0, 0)
    txt = f.read()
    x = re.split("CHAPTER", txt)
    x.pop(0)
    #print(searchQuote)
    ch = 1
    flag = 0
    for chptr in x:
        quotes =[] 
        quotes = re.findall(r'"[^"]*"', chptr, re.U)
        #print(ch, quotes)
        for i in quotes:
            st = " ".join(i.split())
            #print(st)
            if st.strip('"') ==searchQuote:
                print("Found in chapter", ch)
                flag = 1
        
        ch+=1
    if flag == 0:
        print(-1)
        
searchQuote="What can you expect when I have four gay girls in the house, and a dashing young neighbor over the way?"
getChapterQuoteAppears(searchQuote)


# Generate a sentence in authors tone
used =set()
import re
def generateSentence(start):
    #print(used)
    f.seek(0, 0)
    flag =0
    #print(start)
    
    txt = f.read()
    x = re.split(start, txt)
    x.pop(0)
    temp =[]
    #print(x)
    
    for parts in x:
        lst = parts.split()
        if len(lst)==0:
            flag =1
            break
        temp.append(lst[0])
    #print(temp)

    c = set(temp)
    #print(c)
    maxs=0
    word =""
    for wrd in c:
        if wrd not in used:
            if dicts.get(wrd,0)>maxs:
                maxs = dicts.get(wrd,0)
                word = wrd
    #print(word,maxs)
    used.add(word)
    return word

start ="The"
st = "The"
counter=1
while counter<20: 
    rnd = generateSentence(start)
    st+=" "+rnd
    start = rnd
    counter+=1
print(st)





