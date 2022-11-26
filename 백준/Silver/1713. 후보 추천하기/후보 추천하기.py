import sys
from collections import defaultdict

def getPhotoToReplace(recommended, board):
    tempPhoto, tempRecNumber, tempPostedTime = None, float('inf'), 0
    for photo in board:
        recNumber, postedTime = recommended[photo]
        if isLeastRecommendedAndOldest(recNumber, tempRecNumber, postedTime, tempPostedTime):
            tempPhoto = photo
            tempRecNumber = recNumber
            tempPostedTime = postedTime
    return tempPhoto

def isLeastRecommendedAndOldest(recNumber, tempRecNumber, postedTime, tempPostedTime):
    if recNumber < tempRecNumber: return True
    if recNumber == tempRecNumber and postedTime < tempPostedTime: return True
    return False

def updateRecWithoutReplacement(rec, time, recommended):
    if rec in recommended:
        recommended[rec][0] += 1
    else:
        recommended[rec] = [1, time]

def updateRecWithReplacement(rec, time, recommended, key, board):
    board.remove(key)
    recommended[key][0] = 0
    
    board.add(rec)

    if rec in recommended:
        recommended[rec][0] += 1
        recommended[rec][1] = time
    else:
        recommended[rec] = [1, time]
        
input = sys.stdin.readline

N = int(input())
R = int(input())
recs = list(map(int, input().split(' ')))

# 각 학생의 추천된 횟수, board에 올라갔던 시점 관리 : key - 학생 번호 | value - [추천 수, 게시된 시간]
recommended = defaultdict(list)
# 현재 사진이 게시된 학생
board = set()

for time, rec in enumerate(recs):
    if len(board) < N:
        board.add(rec)
        updateRecWithoutReplacement(rec, time, recommended)
    else:
        if rec not in board:
            key = getPhotoToReplace(recommended, board)
            updateRecWithReplacement(rec, time, recommended, key, board)
        else:
            updateRecWithoutReplacement(rec, time, recommended)

print(' '.join(map(str,sorted(list(board)))))
