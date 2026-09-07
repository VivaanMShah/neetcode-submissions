class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for i in nums:
            if i in num_dict.keys():
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        num_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)[0:k]
        result = list(map(lambda x: x[0], num_dict))
        return result