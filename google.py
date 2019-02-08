import csv, bs4
terms = []
with open("list.csv", "r") as file: 
    read = csv.reader(file, delimiter= ' ', quotechar = '|')
    for row in read:
        terms.append(row)
output = []
res = str("gsa.gov")
restrict = [res]
for each in terms:
    from googlesearch import search
    for url in search(query=each, stop=3, domains=restrict):
        print(str(url))
        output.append(str(url))
        
with open("output.csv", "w", newline="") as myfile:
        outputfile = csv.writer(myfile)
        for url in output:
                outputfile.writerow(url)
        myfile.close()