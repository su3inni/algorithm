def solution(cacheSize, cities):
    answer = 0
    cache=[]

    for c in cities :
        c = c.lower()
        # hit
        if c in cache:
            # LRU로 인해 Recently Used Update 필요
            cache.pop(cache.index(c))
            cache.append(c)
            answer+=1
        # miss 
        else:
            if len(cache)<cacheSize:
                cache.append(c)
            # LRU 
            else:
                cache.append(c)
                cache.pop(0)
            answer+=5
    return answer
