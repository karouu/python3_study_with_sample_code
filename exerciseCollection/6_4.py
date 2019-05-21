scoreList = []
sum = 0.

while True:
    score =float(raw_input('pls input a score: '))
    if  score <= 0:
        break
    else:
        scoreList.append(score)
        sum += score
        
print "your average score is %f " % (sum/len(scoreList))
