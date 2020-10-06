# This code is licensed under the GPLv3 by Lorenzo Orders
# https://www.gnu.org/licenses/gpl-3.0.en.html

import json

# returns the number of the first n characters in strB that can be represented
# using consecutive chars in strA
# returns: (# of times to go through strA to construct strB, length of
# strB that can be constrcucted with strA)
def longestLen(strA, strB):
    currentBchar = 0
    iterations = 0
    wordStart = 0
    # if currentBchar is the length of strB, then all of strB can
    # be represented in strA
    
    # if all of strA is iterated through without changing currentBchar
    # then the largest subset 

    # if the tweet needs to be refreshed, go back to the start of the
    # previous word in strB. This prevents words from running onto multiple
    # tweets
    while (True):
        startVal = wordStart
        currentBchar = startVal
        iterations += 1
        for a in strA:
            if (a == strB[currentBchar]):
                currentBchar += 1
                if (currentBchar >= len(strB)):
                    return [iterations, len(strB)]
            if (strB[currentBchar] == ' '):
                wordStart = currentBchar + 1
        if (startVal == wordStart and iterations > 1):
            return [iterations, startVal]

# assuming that collection is sorted descending, this returns the index
# of the second smallest value in collection using binary sort
# if no second smallest exists, it is easiest to return the location of
# the length of the list
def findSecondLargest(collection):
    largest = collection[0]
    maxBound = len(collection) - 1
    minBound = 0
    # if no second smallest exists
    if (largest == collection[maxBound]):
        return maxBound + 1
    while (maxBound - minBound > 1):
        pivotPos = (maxBound + minBound) // 2
        if (collection[pivotPos] < largest):
            maxBound = pivotPos
        elif (collection[pivotPos] >= largest):
            minBound = pivotPos
    if (collection[maxBound] > collection[minBound]):
        return maxBound
    return minBound
    
def main(args):
    lyrics = args[2].lower()
    # each element in storage contains [iters through strA, len of strB, tweet used]
    storage = []
    print("Finding tweets to match:", args[2])
    with open(args[1], encoding='utf-8') as f:
        data = json.load(f)
        for tweet in data:
            result = longestLen(tweet["text"].lower(), lyrics)
            storage.append((result[0], result[1], tweet))
    
    # sort storage by the longest length of the recreated strB, descending
    storage.sort(key = lambda a: a[1], reverse = True)
    
    # slice storage by the longest length of the constructed song lyric
    # so that only the tweets that maximize the length of strB are considered
    secondSmallestPos = findSecondLargest(list(map(lambda a: a[1], storage)))
    storage = storage[:secondSmallestPos]
    # sort the remaining options by the number of times needed to cycle
    # through the tweet, ascending
    storage.sort(key = lambda a: a[0])
    
    # return the best tweet.
    # first print out the length of the input string
    # Print out name, use the ID to make a URL, the length of the new strB,
    # and the number of times to cycle through the tweet.
    print("Closest tweet:", storage[0][2]["text"])
    print("The next two numbers should be identical for best results")
    print("Length of target string:",len(lyrics))
    print("Length of constructed string:",storage[0][1])
    print("Times to cycle through tweet:",storage[0][0])
    print("URL:", "https://twitter.com/realDonaldTrump/status/" + storage[0][2]["id_str"])
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
