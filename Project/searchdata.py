import math

#get index number of specific URL in list of content of readsites.txt
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
    

#get number of times word appears in a certain document
def word_count(word, URL):
    content = open(URL, 'r')
    words = content.readlines()[1].strip().split(',') #read only second line and format
    word_count = 0

    for each in words:
        if each == f'{word}':
            word_count += 1
    
    return word_count

#get total number of unique documents
def total_docs():
    file = open('readsites.txt', 'r')
    link_count = file.readline()
    file.close()
    
    return int(link_count)

#get number of documents containing a specific word
def doc_freq_of_word(word): #CAN IMPROVE RUN TIME MAYBE?
    per_doc_count = 0
    seed = open('readsites.txt', 'r')
    all_links = seed.readlines()

    for all in range(len(all_links)):
        if all == 0: 
            continue #skip lines at top of readsites.txt

        current_link = all_links[all].split('/')
        current = word_count(word, f'{'-'.join([current_link[4],current_link[5].strip('.html\n')])}.txt') #links to relevant text file containing relevant info
        
        if current > 0:
            per_doc_count += 1

    seed.close()
    
    return per_doc_count

def get_idf(word):

    if doc_freq_of_word(word) == 0:
        return 0
    
    idfw = math.log((total_docs()/(1 + doc_freq_of_word(word))), 2)

    if idfw < 0:
        return 0
    return idfw

#fetch total number of words to parse in specific document
def get_total_words(URL):
    page = open(f'{URL}', 'r') #URL already formatted
    words = page.readlines()[1].split(',') #only read second line
    page.close()
    
    return len(words)

def get_tf(URL, word): 
    if find_index(URL) != -1:
        current_URL = f'{'-'.join([URL.split('/')[4],URL.split('/')[5].strip('.html\n')])}.txt' #format URL to match file name
        w_count = word_count(word, current_URL) 
    else: #if URL is not found
        return 0

    if word_count == 0:
        return 0
    
    tfwd = w_count / get_total_words(current_URL)

    return tfwd

def get_tf_idf(URL, word):
    tf_idf_wd = math.log(1 + get_tf(URL, word), 2) * get_idf(word) #must be log base 2 or else answers incorrect: not indicated in project outline but in lessons briefly
    
    return tf_idf_wd

