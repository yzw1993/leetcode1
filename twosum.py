from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i,num in enumerate(nums):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]],i]
        hashmap[nums[i]] = i
    return []


if __name__ == '__main__':
    list = [2,7,11,15]
    target = 9
    print(twoSum(self=None,nums=list,target=target))
    # print(__name__)
