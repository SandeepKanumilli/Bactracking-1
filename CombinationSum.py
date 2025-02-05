
# Time Complexity : O(2^(n+m) * N)
# Space Complexity : O((n+m) * 2^(n+m))

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == None and len(candidates) == 0:
            return []
        self.result = []
        self.recurcive(candidates, target, 0, [] )
        return self.result
    
    def recurcive(self, candidates: List[int], target: int, index: int, path : List[int] ) -> None:
        if(target == 0):
            self.result.append([num for num in path])
            return 
        if index == len(candidates) or target < 0:
            return 
        
        #0 Case

        self.recurcive(candidates, target, index+1, [num for num in path])

        #1 Case
        path.append(candidates[index])
        self.recurcive(candidates, target - candidates[index], index , [num for num in path])
        path.pop()

        