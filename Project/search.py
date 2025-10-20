# ???? idk what i'm doing here pls halp
import searchdata

#multiply 2 matrices
def mult_matrix(a, b): 
	a_rows = (len(a))
	a_cols = len(a[0])
	b_rows = len(b)
	b_cols = len(b[0])

	num_store = 0
	row_store = []
	new_matrix = []

	if a_cols != b_rows:
		return None
	else:
		for i in range(a_rows): #change rows of a for cols of b
			for k in range(b_cols): #repeat for all cols of b
				for j in range(b_rows): #change in rows of b
					num_store += (a[i][j] * b[j][k]) #change y of a and x of b at same time

				row_store.append(num_store)
				num_store = 0

			new_matrix.append(list(row_store)) #list() to avoid variable changing values inside mutable list
			row_store.clear()

	return new_matrix

#calculate euclidean norm using 2 points (sets of ordinates) in the nth dimension
def euclidean_dist(a):
	#import math
	eucl_dist = 0

	for dimens in range(len(a)):
		eucl_dist += a[dimens] ** 2
	#eucl_dist = (eucl_dist) ** 0.5
	return eucl_dist ** 0.5

#TREAT QUERY EXACTLY LIKE A DOCUMENT
#get vector score of a specific word for a document
#for links in all_links: 
def vectorize(word, document):
#get vector score of a specific word for all documents in order of appearance in readsites.txt
def vectorize(word):
    seed = open('readsites.txt', 'r')
    all_links = seed.readlines()[1:] #from index [1] onward
    vector = []

    vector.append(searchdata.get_tf_idf(document.strip('\n'), word))
    return vector

def cos_similarity(query, document):
    numerator = mult_matrix(query, document)#????? 
    denominator = euclidean_dist(query) * euclidean_dist(document) #relate to vectorize function, basically same thing?? maybe??? i hope???????

    if numerator == 0 or denominator == 0: #I don't think this would work????
        return 0
    return numerator / denominator

def search(phrase, boost):
    list_query = phrase.split(' ')
    #'url' = 'absolute-link'
    #'title' = 'N-X' format?
    #'score' = float value
    top10 = [{'url': '', 'title': '', 'score': 0}, {}] #top 10 ranked search results, sorted highest to lowest

    query = []
    for word in list_query:
        query.append(searchdata.get_tf_idf(word))

    pagerank_file = open('pagerank.txt', 'r')
    pages_ranked = pagerank_file.readline().split(', ')
    #format: [0] = N-0.txt -> [n] = N-n.txt

    for document in len(pages_ranked):

        final_score[document] = {}
        final_score[document]['score'] = PLACHOLDER
        if boost == True:
            final_score = content_score * get_page_rank(URL) 
    
    pagerank_file.close()
    return top10[0:10] #stop before index [10]