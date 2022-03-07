def scores_of_players(list_scores):
    p1,p2,flag=0,0,0
    
    for i,num in enumerate(list_scores):
        if i<6:
            if flag==0:
                p1+= num
                if num%2 !=0: flag=1   

            elif flag==1:
                p2+= num
                if num%2 !=0: flag=0   
        else: 
            if i%2 ==0:
                p1+= num
            else:
                p2+= num

                
    print(f'p1: {p1}, p2: {p2}') 
 
if __name__== '__main__':
    print("---Start Task---")
    
    data=[1,2,3,2,1]
    scores_of_players(data)
    
    '''if user input data '''
   # data=input()[1:-1].split(',')
   # scores_of_players([int(i) for i in data])
    
             

                
            
            
            
    