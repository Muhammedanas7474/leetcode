class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for start in range(n):
            for end in range(start, n):
                
                if (end - start + 1) % 2 != 0:

                    total_sum += sum(arr[start:end+1])
                    
        return total_sum
            

        