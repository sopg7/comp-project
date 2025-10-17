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
    