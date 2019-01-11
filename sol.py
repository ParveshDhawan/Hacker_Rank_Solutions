# Based on Some Ranking find Out who Win!!
#######################################################
def aa(erica,bob):
    score = {'S':0,'E':1,'M':3,'H':5}
    e_score_list = [score[i] for i in erica]
    b_score_list = [score[i] for i in bob]
    if sum(e_score_list) < sum(b_score_list):
        print('bob')
    elif sum(e_score_list) > sum(b_score_list):
        print('erica')
    else:
        print('tie')

aa('ESM','EHM')
#########################################################

# Giving a list find the count of tupples where sum = 60, 
# !!! Note touple counts so it should not be like a number on the same index inside the list :-)
def playlist(songs):
    counter = 0
    for i in range(len(songs)):
        for j in range(len(songs)):
            if (songs[i] + songs[j]) == 60 and i != j:
                counter += 1
    
    return counter 
    
li = [4,10,50,90,30]
playlist(li)

######################################################

