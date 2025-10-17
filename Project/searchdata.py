def find_index(URL):
    f = open('readsites.txt','r')
    data = f.readlines()
    f.close()
    if f'{URL}\n' in data:
        index_URL = data.index(f'{URL}\n')
        return index_URL - 1
    else:
        return -1

def get_outgoing_links(URL):
    index = find_index(URL)
    if index != -1:
        f = open('outgoing.txt','r')
        data = f.readlines()
        outgoing = (data[index]).strip('\n').split(',')
        return outgoing
    else:
         return None
def get_incoming_links(URL):
    index = find_index(URL)
    if index != -1:
        f = open('incoming.txt','r')
        data = f.readlines()
        incoming = (data[index]).strip('\n').split(',')
        return incoming
    else:
         return None

def get_page_rank(URL):
    index_URL = find_index(URL)
    f = open('pagerank.txt','r')
    page_ranks = (f.readline()).split(', ')
    if index_URL != -1:
        return float(page_ranks[index_URL])
    else:
        return -1
    

#---------------------------------------------------

#PREVIOUS CODE ABOVE COMPELETED BY SOPHIE
import math

#what documents we have:
#outgoing.txt = file of outgoing links for each link
#incoming.txt = file of incoming links for each link
#pagerank.txt = file of ranks of each link?
#readsites.txt = file of all files crawled thru + total link count
# all N-X.txt = files of content of each link

#get number of times word appears in a certain document
def word_count(word, URL):
    content = open(URL, 'r') #align formatting of URL w/ Sophie's formatting
    words = content.strip().split(',')
    word_count = 0

    for each in words:
        if each == f'{word}':
            word_count += 1
    
    return word_count

#get number of documents containing a specific word
def doc_freq_of_word(word):
    per_doc_count = 0
    seed = open('readsites.txt', 'r')
    total_links = int(seed.readline().strip())
    all_links = seed.readlines()

    for all in range(seed):
        current = word_count(word, f'{(all_links[all].split('/'))[5].strip('.html\n')}.txt') #links to relevant text file containing relevant info
        if current > 0:
            per_doc_count += 1

    seed.close()
    return per_doc_count


def get_idf(word):

    if doc_freq_of_word(word) == 0:
        return 0
    
    idfw = math.log((totalDocs/(1 + doc_freq_of_word(word))), 2)

    if idfw < 0:
        return 0
    return idfw

def get_tf(URL, word):
    tCount = 0
    wCount = 0

    #for items in URL:
    #    tCount += 1
    #    if items == word:
    #        wCount +=  1

    if URL not in wordCount:
        return 0
    
    #OR: if dict of URL w/ docFreq[word] + wordCount[doc] already made:
    tfwPerDoc = docFreq[word] / wordCount[URL]

    if wCount == 0:
        return 0

   #tfwPerDoc = wCount / tCount
    return tfwPerDoc

def get_tf_idf(URL, word):
    tf_idf = log(1 + get_tf(URL, word)) * get_idf(word)
    return tf_idf

