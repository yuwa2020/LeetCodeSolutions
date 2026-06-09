class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h_index = 0
        # while (h_index <= len(citations)):
        #     count = sum(1 for x in citations if x > h_index)
        #     print(h_index, count)
        #     if count >= h_index + 1:
        #         h_index += 1
        #     else:
        #         return h_index
        
        # return h_index


        # [3,0,6,1,5]

        # n * n 

        citations.sort(reverse=True)
        length = len(citations)
        if citations[0] == 0:
            return 0
        num = 1
        print(citations)
        while (num <= length):
            print(num, index, citations[num-1])
            if citations[num-1] >= num:
                num += 1
            else:
                return num - 1
            if num == length:
                if citations[num-1] >= num:
                    return num
                else:
                    return num -1
        
        return num - 1






