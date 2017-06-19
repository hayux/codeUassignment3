# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:41:11 2017

@author: hexu
"""

def findword(nRow, nCol, charArray, myDict):
    """
    input:
    nRow -- number of rows
    nCol -- number of columns
    charArray -- 2d array contains only chars, can be duplicated chars
    myDict -- an instance of the dictionaly class, contains a list of words, isWord(), isPrefix()
    
    output:
    myWords -- words found in charArray, no duplication
    """
    # initialize myWord colellection (set, avoid duplication)    
    myWords = set();
    
    for r in range(nRow):
        for c in range(nCol):
            # start searching on each location
            
            # -- get the char from current location, the starting of a possible word
            myChar = charArray[r][c]
            
            # -- if myChar is the prefix of a word, then continue searching the adjacent chars, otherwise stop, go to next char
            if myDict.isPrefix(myChar):
                # continue searching
                # initialize the searching map to store the visited locations
                searchMap = [[r,c]]
                resultWords = localSearchWord(charArray, myDict, searchMap)
                myWords.add(resultWords)
            else:
                continue
    
    return myWord
    
def localSearchWord(nRow, nCol, charArray, myDict, searchMap):
    """
    steps:
    1. find the last location (r,c) in the searchMap
    2. make the neighbour list of (r,c)
    3. construct the string formed by searchMap and the neighbouring chars of last location
    4. if isPrefix(string) == True, go to 5, if not, quit searching, return empty
    5. if isWord(string) == True, return word, keep searching until kit the charArray limit
    
    input:
    charArray, myDict
    searchMap -- 2d array, contains all the searched locations which forms the prefix of myDict
    
    output:
    resultWord
    
    """
    # if the length of searched word is larger than the longest word in dictionary, stop searching
    if len(searchMap)>len(max(myDict.words, key=len)):
        return None
    
    # initialize word collection
    collection = set();

    # -- find the last location searched, contains the index of row and coloum
    lastLocation = searchMap[-1]
    
    # -- make the neighbour list, try 8 directions and find all possible neighbours
    neighbourList = findNeighbours(nRow, nCol, lastLocation)
    
    # -- make sure that we don't visit the same cell again when adding neighbours
    for neighbour in neighbourList:
        if neighbour in searchMap:
            neighbourList.remove(neighbour)
            
    # if there is no neighbour, then stop searching and return        
    if len(neighbourList) == 0:
        return None
        
    # -- construct the sting with neighbouring chars
    wordCandidate = formString(charArray, searchMap, neighbourList)
    
    # -- see if any of the candidate is a prefix in the dictionary
    for candidate in wordCandidate:
        if myDict.isPrefix(candidate):
            # is a prefix in the dictionary
            # -- add the neighbour location into searchMap and continue search with searchMap           
            searchMap.append(neighbourList[wordCandidate.index(candidate)])
            
            # add candidate into word collection if it is a word
            if myDict.isWord(candidate):
                collection.add(candidate)
            
            # still need to keep searching for the prefix unitl it forms a word or no possible neighbours anymore
            collection.add(localSearchWord(nRow, nCol, charArray, myDict, searchMap))
        else:
            # is not a prefix, stop searching here
            continue
        
def findNeighbours(nRow, nCol, lastLocation):
    """
    return the 8 possible neighbours of last location
    
    requirements for neighbours (r,c):
        1. r>=0 and c>=0
        2. r<nRow and c<nCol
        
    input:
        nRow -- number of rows
        nCol -- number of cols
        lastlocation -- a list with 2 element, lastlocation[0] = row axis, lastlocation[1] = col axis

    output:
        neighourList -- a list contains all legal neighbour locatiosn, in the form [[x1,y2],[x2,y2],...]
        
    """
    
    neighbourList = []

    r = lastlocation[0]
    c = lastlocation[1]
    
    for nr in [r-1,r,r+1]:
        for nc in [c-1,c,c+1]:
            if nr>=0 and nr<nRow:
                if nc>=0 and nc<nCol:
                    neighbourList.append([nc,nr])
                    
    neighbourList.remove([r,c])
    return neighbourList

def formString(charArray, searchMap, neighbourList):
    """
    form a string from visited locations on charArray
    
    input:
        charArray -- 2d array, contains a char in each cell, chars can be duplicated
        searchMap -- a list of visited locations on charArray, no duplication
        neighbourList -- a list of neighbouring locations of the last visited location, non-empty

    output:
        candidates -- a list of strings contains the candicates of forming a word
    """
    
    candidate = []
    # construct the prefix of candidates, using all locations in searchMap
    prefix = ''
    
    for location in searchMap:
        prefix = prefix + charArray[location[0]][location[1]]
    
    # adding neighbouring chars into prefix to form candidates
    for neighbour in neighbourList:
        tempWord = prefix + charArray[neighbour[0]][neighbour[1]]
        candidate.append(tempWord)
        
    return candidate
    
    
    
nRow = 2
nCol = 3
charArray = [[A,A,R],[T,C,D]]
myDict.words = ['CAT','CAR','CARD']
assert findword(nRow, nCol, charArray, myDict)     
    
    
    
    
    
    
    
    
    
    
    
    
    
