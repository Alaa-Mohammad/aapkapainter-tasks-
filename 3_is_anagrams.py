from collections import Counter

def is_anagrams(word1,word2):
    if Counter(word1.lower())==Counter(word2.lower()):
        print("Yes")
    else:
        print("No")
        
if __name__== '__main__':
    print("---Start Task---")
    
    is_anagrams('Mary','Army')
    
    '''if user input data '''
    #w1,w2=input().split()
    #is_anagrams(w1,w2)

    
                