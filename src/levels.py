from random  import randint
def session_sets():
    s = []
    '''
    s.append([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4])
    s.append([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
    s.append([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4])
    s.append([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4])
    s.append([2,2,2,2,3,3,3,3,1,1,1,1,4,4,4,4,3,3,3,3,2,2,2,2,1,1,1,1,4,4,4,4])
    s.append([3,2,1,4,2,3,1,4,4,2,1,3,1,3,4,2,4,3,2,1,2,1,4,3,2,3,4,1,3,2,4,1])
    s.append([4,4,4,4,3,3,3,3,2,2,2,2,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,1,1,1,1])
    s.append([3,3,2,2,1,1,4,4,2,2,4,4,3,3,1,1,2,2,4,4,3,3,1,1,3,3,1,1,2,2,4,4])
    s.append([4,2,1,3,2,3,1,4,3,2,4,1,2,4,1,3,3,2,4,1,3,2,1,4,4,3,1,2,3,4,2,1])
    s.append([4,4,3,2,1,3,4,2,1,2,3,4,2,1,3,1,4,2,1,2,3,4,3,2,1,1,3,4,3,2,1,4])
    s.append([3,2,4,1,2,3,4,1,1,1,3,4,2,1,4,3,4,3,2,1,4,2,4,3,1,2,3,4,2,1,2,3])
    s.append([3,2,4,1,3,2,1,4,2,1,3,4,2,1,4,4,3,1,4,2,3,1,4,2,3,2,3,4,1,2,1,3])
    s.append([3,2,4,4,3,1,3,2,1,4,2,1,3,1,4,2,3,1,2,3,4,2,1,4,3,4,1,2,4,1,3,2])
    s.append([3,1,4,1,3,2,1,3,2,4,1,4,4,2,1,3,2,2,3,1,4,3,2,4,1,2,3,4,2,3,4,1])
    s.append([1,1,2,3,4,2,3,1,2,3,4,1,4,2,1,3,4,1,4,1,4,1,3,3,2,4,2,3,4,2,3,2])
    s.append([2,1,3,1,4,2,4,3,1,4,2,3,1,4,2,3,4,1,2,3,4,2,3,1,4,3,2,3,1,2,4,1])
    s.append([3,2,3,1,1,4,2,3,1,4,2,3,1,4,2,4,1,3,2,3,4,1,2,3,1,4,2,3,4,1,2,4])
    '''
    #s.append([2,1,3,1,4,2,4,3,1,4,2,3,1,4,2,3,4,1,2,3,4,2,3,1,4,3,2,3,1,2,4,1])
    #s.append([1,2,3,4])
    s.append([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4])

   # print  len(s)
    #for i in s:
     #   print i.count(1),i.count(2),i.count(3),i.count(4)
    num = randint(0,len(s)-1)
    #print num
    return s[num]




#x = session_sets()
#print x