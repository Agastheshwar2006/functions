def countWordsFromfile():
    filename=input('Enter the file name:')
    numberOfwords=0
    file=open(filename, 'r')
    for i in file :
        words=i.split()
        numberOfwords=numberOfwords+len(words)
    print("Number of words: ")
    print(numberOfwords)

countWordsFromfile()