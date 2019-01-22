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
# Matching pair inside the list
def sockMerchant(n, ar):
    uniq_final = 0
    counter = 0
    count = 0
    uniq = list(set(ar))
    for i in uniq:
        for j in range(n):
            if i == ar[j]:
                counter += 1
        final = counter // 2
        counter = 0
        count += final
        #print(count)
    return count

#####################################################
# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count = 0
    level = 0
    for i in s:
        #going downside
        if i == 'U':
            level += 1
            
        # still in the valley it will be 1 
        elif i == 'D':
            level -= 1
            if level == -1:
                valley_count += 1
            
    return valley_count

li = "UDDDUDUU"
countingValleys(len(li),li)
#output = 1
#If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:
# _/\      _
#    \    /
#     \/\/
######################################################

#Drawing Book --Find the page number w.r.t min turns:
##here n=  total pages //   p = page number
def count_turn(n,p):
    return min(p // 2, n //2 - p // 2)
    
##########################################################################
## Electronic Shop :- sum of two list element and check for specific amount condition

def getMoneySpent(keyboards, drives, b):
    combo = []
    final = []
    for i in keyboards:
        for j in drives:
            combo.append(i+j)
    combo = set(combo)
    for l in combo:
        if l <= b:
            final.append(l)
    if len(final) == 0:
        return -1

    return max(final)

## Another Approch ###------
def gms(keyboards, drives, b):
    final_spent = -1
    for i in keyboards:
        for j in drives:
            if(i + j <= b):
                final_spent = max(final_spent, i + j)

    return final_spent

##########  o/p
getMoneySpent([3,1],[5,2,8],10)
#10 2 3
#3 1
#5 2 8
#ans will be 8 + 1= 9

##################################################################
