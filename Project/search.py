# ???? idk what i'm doing here pls halp
import searchdata
import math

tf_idfs = []
final_score = [{'score': 0}]

#sort 2D list from highest to lowest w/ selection sort
def sort_highest(list_2d):
    new_list = list_2d
    
    for element in range(len(new_list)):
        maximum = element #start of unsorted

        #find largest value in unsorted
        for unsorted in range(element + 1, len(new_list)):
            if 'score' not in new_list[unsorted]: 
                continue
            if new_list[unsorted]['score'] > new_list[maximum]['score']:
                maximum = unsorted

        #swap only once per iteration
        if maximum != element:
            new_list[element], new_list[maximum] = new_list[maximum], new_list[element]

    return new_list

def cos_similarity(query, link):
    numerator = 0
    left_denom = 0
    right_denom = 0

    for term in range(len(query)):
        term_freq = searchdata.get_tf(link, query[term])
        numerator += term_freq * tf_idfs[term]
        left_denom += tf_idfs[term] ** 2            
        right_denom += term_freq ** 2 #NOT TF_IDF

    if left_denom == 0 or right_denom == 0:
        return 0
    else:
        return (numerator / (left_denom * right_denom) ** 0.5) #output score for document in relation w/ query

def search(phrase, boost):
    #'url' = 'absolute-link'
    #'title' = 'N-X' format?
    #'score' = float value
    global final_score
    #top 10 ranked search results, sorted highest to lowest
    global tf_idfs
    tf_idfs = []
    cos_simi = []
    list_query = phrase.split(' ')

    seed = open('readsites.txt', 'r')
    all_links = seed.readlines()[1:] #from index [1] onward
    seed.close()
    pagerank_file = open('pagerank.txt', 'r')
    pages_ranked = pagerank_file.readline().split(', ')
    #format: [0] = N-0.txt -> [n] = N-n.txt
    pagerank_file.close()


    #make query accessible to get_tf and get_idf functions
    query_file = open('query.txt', 'w')
    for item in range(len(list_query)):
        query_file.write(f'{list_query[item]}')
        if item != len(list_query) - 1: #do not add comma at end of query
            query_file.write(',')

    query_file.close()

    #calculate tf_idf of all items in query and put into list
    for item in list_query:
        tf_idfs.append(math.log(1 + searchdata.get_tf('query.txt', f'{item}')) * searchdata.get_idf(item))
    
    #calculate cosine similarities for all documents and put into list
    for link in range(len(all_links)):
        cos_result = cos_similarity(list_query, all_links[link])
        cos_simi.append([link, cos_result])

    for order in range(len(cos_simi)):
        final_score.append({})
        final_score[order]['score'] = cos_simi[order][1]
        final_score[order]['url'] = all_links[cos_simi[order][0]].strip('\n')
        file_holder = all_links[cos_simi[order][0]].split('/')
        infile = open(f'{'-'.join([file_holder[4],file_holder[5].strip('.html\n')])}.txt', 'r')
        final_score[order]['title'] = infile.readline().strip('<p>\n')

        if boost == True:
            final_score[order]['score'] = cos_simi[order][1] * searchdata.get_page_rank(final_score[order]['url']) 

    final_score = sort_highest(final_score)
        
    return final_score[:10] #stop before index [10]



