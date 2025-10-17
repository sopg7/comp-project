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

def get_idf(word):

    if docFreq[word] == 0:
        return 0
    
    #gotta really see what the previous code looks like before actually making more of this
    #idfw = math.log((totalDocs/(1 + docFreq[word])), 2)

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

