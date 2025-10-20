# ???? idk what i'm doing here pls halp
import searchdata

#get vector score of a specific word for all documents in order of appearance in readsites.txt
def vectorize(word):
    seed = open('readsites.txt', 'r')
    all_links = seed.readlines() #<--- skip first line [1:]???
    vector = []

    for links in all_links: 
        vector.append(searchdata.get_tf_idf(links.strip('\n'), word))
    return vector

def search(phrase, boost):
    list_query = phrase.split(' ')
    #'url' = 'absolute-link'
    #'title' = 'N-X' format
    #'score' = float value
    top10 = [{'url': '', 'title': '', 'score': 0}, {}] #top 10 ranked search results, sorted highest to lowest

    query = cos_similarity(???)

    pagerank_file = open('pagerank.txt', 'r')
    pages_ranked = pagerank_file.readline().split(', ')
    #format: [0] = N-0.txt -> [n] = N-n.txt

    for document in len(pages_ranked):

        final_score[document] = {}
        final_score[document]['score'] = PLACHOLDER
        if boost == True:
            final_score = content_score * get_page_rank(URL) 
    
    pagerank_file.close()
    return top10[0:9] #<--- is that the correct notation??