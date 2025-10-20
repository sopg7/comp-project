# ???? idk what i'm doing here pls halp
import searchdata

#sort 2D list from highest to lowest w/ selection sort
def sort_highest(list_2d):
    new_list = list_2d

    for element in range(len(new_list)):
        maximum = element #start of unsorted

        for unsorted in range(maximum + 1, len(new_list)):
            if new_list[unsorted][1] < new_list[maximum][1]:
                maximum = unsorted

            if maximum != unsorted:
                new_list.insert(maximum, new_list[unsorted])
                new_list.pop(unsorted + 1)

        #check 1st and 2nd indices one last time (it misses this step)
        if new_list[0][1] < new_list[1][1]:
            new_list.insert(0, new_list[1])
            new_list.pop(2)

    return new_list

def cos_similarity(query, link):
    numerator = 0
    left_denom = 0
    right_denom = 0

    for term in range(len(query)):
        term_freq = get_tf(link, query[term])
        numerator += term_freq * tf_idfs[term]
        left_denom += tf_idfs[term] ** 2            
        right_denom += term_freq ** 2 #CHECK IF THIS IS TERM FREQ OR TF_IDF

    cos_simi.append(numerator / (left_denom * right_denom) ** 0.5)

    return cos_simi #output score for document in relation w/ query

def search(phrase, boost):
    list_query = phrase.split(' ')
    #'url' = 'absolute-link'
    #'title' = 'N-X' format?
    #'score' = float value
    final_score = [{'url': '', 'title': '', 'score': 0}, {}] #top 10 ranked search results, sorted highest to lowest
    tf_idfs = []
    seed = open('readsites.txt', 'r')
    all_links = seed.readlines()[1:] #from index [1] onward
    seed.close()
    cos_simi = []
    pagerank_file = open('pagerank.txt', 'r')
    pages_ranked = pagerank_file.readline().split(', ')
    #format: [0] = N-0.txt -> [n] = N-n.txt
    pagerank_file.close()


    #make query accessible to get_tf and get_idf functions
    query_file = open('query.txt', 'a')
    for item in range(len(list_query)):
        query_file.write(f'{list_query[item]}')
        if item == len(list_query): #do not add comma at end of query
            continue
        
        query_file.write(',')

    query_file.close()

    #calculate tf_idf of all items in query and put into list
    for item in list_query:
        tf_idfs.append(math.log(1 + get_tf('query.txt', f'{item}')) * get_idf(item))
    
    #calculate cosine similarities for all documents and put into list
    for link in range(len(all_links)):
        cos_result = cos_similarity(list_query, all_links[link])
        cos_simi.append([link, cos_result])

    cos_simi = sort_highest(cos_simi)

    for order in range(len(cos_simi)):
        final_score[order] = {}
        final_score[order]['score'] = cos_simi[order][1]
        final_score[order]['url'] = all_links[cos_simi[order][0]]
        file_holder = all_links[cos_simi[order][0].split('/')
        infile = open(f'{'-'.join([file_holder[4],file_holder[5].strip('.html\n')])}.txt', 'r')
        final_score[order]['title'] = infile.readline()

        if boost == True:
            final_score[order]['score'] = content_score * get_page_rank(final_score[order]['url']) 
        
    return final_score[:10] #stop before index [10]
