# ???? idk what i'm doing here pls halp
def search(phrase, boost):
    listPhrase = phrase.split(" ")
    top10 = [{"url": "", "title": "", "score": 0}, {}] #top 10 ranked search results, sorted highest to lowest

    for #each word in phrase:
        #for eachDoc in allDocs where docFreq[word] > 0:
            #get docFreq[word]
            #calculate cosine similarity???(what is that)
    
            if boost == True:
                #contentScore = cosineSimilarityScore
                overallScore = contentScore * get_page_rank(eachDoc)
            
            top10.append({"url": url, "title": title, "score": overallScore})

    #SORT top10 FROM HIGHEST TO LOWEST
    #PLACEHOLDER ---> probably do bucket sort
    #buckets: scores: 0-x/8, x/8-x/4, x/4-3x/8, 3x/8-x/2, x/2-5x/8, 5x/8-3x/4, 3x/4-7x/8, 7x/8-x WHERE x is highest score
    #sort into buckets
    #sort each bucket from highest to lowest, only needing all buckets up until ~top 10th score
    #top10 = [bucket8+bucket7+bucket6+bucket5+bucket4+bucket3+bucket2+bucket1]

    #while len(top10) > 10:
    #    top10.pop(-1)

    return top10[0:9] #<--- is that the correct notation??