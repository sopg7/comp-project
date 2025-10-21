from webdev import read_url

# Opens readsites.txt and reads the data from it
# Inputs: none
# Outputs: number of sites/files for sites (num_files) and all raw data (data)
def readsites_data():
    f = open('readsites.txt','r')
    data = f.readlines()
    num_files = int(data[0].strip('\n'))
    f.close()

    return num_files, data

# Turns a link into its text file name
# Inputs: link
# Outputs: text file name (ex: N-1.txt)
def txt_name(link):
    link = link.split('/')
    return f'{'-'.join([link[4],link[5].strip('.html\n')])}.txt'

# Finds all outgoing links from a website
# Inputs: which site to find the outgoing links for (URL)
# Outputs: list of all outgoing links (outgoing)
def find_outgoing_links(URL):
    outgoing = []
    f = open(txt_name(URL),'r')
    outgoing = f.readlines()[3:]
    for s in range(len(outgoing)):
            outgoing[s] = outgoing[s].strip('\n')

    f.close()

    if len(outgoing) >= 1:
        return outgoing
    else:
        return None
		
# Finds all incoming links for a website
# Inputs: which site to find incoming links for (URL)
# Outputs: list of all incoming links (incoming)
def find_incoming_links(URL):
    incoming = []
    num_files,data = readsites_data()

    for x in range(1,len(data)):
        f = open(txt_name(data[x]),'r')
        file_links = f.readlines()
        if f'{URL}\n' in file_links and file_links[2].strip('og:\n') not in incoming and f'{URL}\n' != file_links[2].strip('og:'):
            incoming.append(file_links[2].strip('og:\n'))
        f.close()

    if len(incoming) >= 1:
        return incoming
    else:
        return None

# Multiplies a matrix by a scalar value.
# Inputs: matrix, scalar value (scale)
# Outputs: copy of matrix after multiplication by scalar value
def mult_scalar(matrix, scale):
	copy = matrix

	for x in copy:
		for y in range(0,len(x)):
			value = x[y]
			x[y] = scale*value

	return copy

# Multiplies 2 matrices
# Inputs: matrix a, matrix b
# Output: product of matrix a and b OR None if they can't be multiplied
def mult_matrix(a, b):
	if len(a[0]) == len(b):
		product = []

		for x in range(len(a)):
			row = []

			for i in range(len(b[0])):
				sum = 0

				for y in range(len(b)):
					sum+=a[x][y]*b[y][i]

				row.append(sum)

			product.append(row)

		return product
	else:
		return None

# Calculates euclidian distance between 2 matrices
# Inputs: matrix a, matrix b
# Outputs: distance between matrix a and b OR None if they don't have an equal amount of rows
def euclidean_dist(a, b):
	if len(a) == len(b):
		sum = 0

		for x in range(len(a)):
			for y in range(len(a[0])):
				sum += (a[x][y]-b[x][y]) ** 2

		distance = sum ** 0.5

		return distance
	else:
		return None

# Calculates all page ranks for sites in the crawl
# Inputs: none
# Outputs: list of all page ranks (current)
def calc_page_ranks():
    num_sites,data = readsites_data()
    matrix = []
    vector = []
    innerVector = []

    for x in range(num_sites):
        innerVector.append(1/num_sites)
        link = data[x+1].strip('\n')
        outgoing = find_outgoing_links(link)
        row = []

        for s in data[1:]:
            site = s.strip('\n')

            if site in outgoing:
                row.append(1)
            else:
                row.append(0)

        if all(e == 0 for e in row) == True:
            for e in range(len(row)):
                row[e] = 1/num_sites
        else:
            num1 = row.count(1)
            rowSum = 0

            for e in range(len(row)):
                if row[e] == 1:
                    row[e] = 1/num1

                rowSum+=row[e]

        matrix.append(row)

    matrix = mult_scalar(matrix,0.9)

    for x in matrix:
        for y in range(len(x)):
            x[y] += 0.1/num_sites

    vector.append(innerVector)
    prev = mult_matrix(vector,matrix)
    current = mult_matrix(prev,matrix)
    distance = 1

    while distance > 0.0001:
        prev = current
        current = mult_matrix(prev,matrix)
        distance = euclidean_dist(prev,current)

    return current

def make_link(raw, link):
    raw = raw.replace('href=','')
    raw = raw.replace('"','')
    if 'https://' not in raw:
        raw = raw.replace('./',('/'.join(link[:5])+'/'))
    elements = raw.split('>')
    if len(elements) >= 1:
        raw = elements[0]
    return raw

def crawl(seed):
    read_sites = []
    sites = [seed]
    data = ''

    while len(sites) > 0:
        data = read_url(sites[0])
        data = data.split()
        start = []
        stop = []
        writing = []
        text = []
        link = sites[0].split('/')
        title_start = 0
        title_stop = 0
        for x in range(len(data)):
            if '<title>' in data[x]:
                title_start = x
            if '</title>' in data[x]:
                title_stop = x
            if '<p>' in data[x]:
                start.append(x+1)

            if '</p>' in data[x]:
                stop.append(x)

            if 'href=' in data[x]:
                data[x] = make_link(data[x],link)
                writing.append(data[x])

                if data[x] not in sites and data[x] not in read_sites:
                    sites.append(data[x])

        while len(start) > 0:
            text.append(','.join(data[start[0]:stop[0]]))
            start.pop(0)
            stop.pop(0)
        title = ' '.join(data[title_start:title_stop+1])
        title.strip(' ')
        title = title.replace('<html><head><title>','')
        title = title.replace('</title></head><body>','')
        writing.insert(0,f'og:{sites[0]}')
        writing.insert(0,','.join(text))
        writing.insert(0,title)
        f = open(txt_name(sites[0]),'w')
        f.write(f'{'\n'.join(writing)}\n')
        f.close()
        read_sites.append(sites[0])
        sites.pop(0)

    f = open('readsites.txt','w')
    f.write(f'{len(read_sites)}\n{'\n'.join(read_sites)}\n')
    f.close()
    incoming = []
    outgoing = []

    for x in read_sites:
        if find_incoming_links(x) != None:
            incoming.append(','.join(find_incoming_links(x)))
        if find_outgoing_links(x) != None:
            outgoing.append(','.join(find_outgoing_links(x)))
    page_ranks = calc_page_ranks()[0]
    pages = [incoming,outgoing,page_ranks]
    page_names = ['incoming','outgoing','pagerank']

    for x in range(3):
        if x == 2:
            writing = str(page_ranks).strip('[]')
        else:
            writing = f'{'\n'.join(pages[x])}\n'

        f = open(f'{page_names[x]}.txt','w')
        f.write(writing)
        f.close()
        
    return len(read_sites)
