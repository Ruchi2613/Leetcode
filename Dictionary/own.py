a = 'aaaddccggggl'

class maxtopk3:

    def topk(self,a):

        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        result = sorted(d.items(), key=lambda x: (x[1], x[0]))
        print('Hey:',result)
        # method 1:

        print(d)
        k = 3
        # new_sorted = sorted(d.items(), key = lambda x : (x[0],x[-1]), reverse = True)
        '''
        ans = []
        new_sorted = sorted(d.items(), key = lambda x : x[1],reverse=True)
        print(new_sorted)
        for key , v in new_sorted:
            if k > 0:
                ans.append(key)
                k -=1
        return ans
        '''

        # method 2: heapq
        import heapq

        heap = []
        for key , v in d.items():
            heapq.heappush(heap,(v,key))
        

            while len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for i in heap:
            ans.append(i[1])
        return ans


c = maxtopk3()
print(c.topk('aaaddccggggl'))