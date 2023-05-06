def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrongest = max(yourLeft, yourRight)
    yourWeakest = min(yourLeft, yourRight)
    friendStrongest = max(friendsLeft, friendsRight)
    friendWeakest = min(friendsLeft, friendsRight)

    return yourStrongest == friendStrongest and yourWeakest == friendWeakest
