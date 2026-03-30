class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucketsort
        # put them into buckets based on the number of time thye show up
        # So if they show up once, you would put them in index 1 or index 
        # 0 just because we're using one base index and the array will be 
        # size... actually I don't know the largest k value, your largest 
        # and nums value. After we put them into all the buckets, 
        # we will just return the last k from the bucket array. 
        # If it's not zero then we add it to a list and return that

        res = [[] for _ in range(len(nums) + 1)]

        # create a freqMap of nums
        freqMap = Counter(nums)
        # loop through keys of freqMap and place the key
        # into res[value], 1 indexed
        # return k from the end of res if not 0
        for i in freqMap.keys():
            res[freqMap[i] - 1].append(i)

        count = 0
        actualRes = []
        print(res)
        for i in range(len(res) - 1, -1, -1):
            print("Count" + str(count))
            if count == k:
                break
            for num in res[i]:
                actualRes.append(num)
                count += 1
        
        return actualRes
            




