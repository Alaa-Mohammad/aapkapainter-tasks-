def find_first_duplicate(nums):
    num_list=list()
    for i in nums:
        if i in num_list:
            return i
        else:
            num_list.append(i)

    return 'no_duplicate'    
    
    
if __name__== '__main__':  
    print("---Start Task---")

    data=[1,2,3,1]
    print(find_first_duplicate(data))
    
    '''if user input data '''
   # data=input()[1:-1].split(',')
    #print(find_first_duplicate([int(i) for i in data]))