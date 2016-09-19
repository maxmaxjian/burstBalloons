'''
Created on Sep 19, 2016

@author: jianwei
'''

import copy

class solution:
    def mostCoins(self, nums):
        return self.mostCoins_recur(nums)
        
    def mostCoins_recur(self, nums):
        if len(nums) == 1:
            coins = nums[0]
        elif len(nums) > 1:
            cands = []
            for i in range(len(nums)):
                if i == 0:
                    curr = nums[i]*nums[i+1]
                elif i == len(nums)-1:
                    curr = nums[i]*nums[i-1]
                else:
                    curr = nums[i-1]*nums[i]*nums[i+1]
                cpy = copy.copy(nums)
                del cpy[i]
                cands.append(curr+self.mostCoins_recur(cpy))
            
            coins = max(cands)
        return coins

def main():
    balloons = [3,1,5,8]
    
    soln = solution()    
    mCoins = soln.mostCoins(balloons)
    
    print("The most coins can be obtained are:", mCoins)
    

if __name__ == '__main__':
    main()