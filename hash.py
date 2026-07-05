# population = dict()
# population["Bhopal"] = 300000
# population["Indore"] = 200000
# population["Delhi"] = 200000
# print(population)
# for city , pop in population.iteam():

nums = [1,1,2,4,3,4,3,2,4,2,5]
counts = dict()

for n in nums:
    if not n in counts:
        counts[n]=0
    counts[n]+=1
print(counts)

 - 2nd method
from collections import defaultdict
nums = [1,1,2,4,3,4,3,2,4,2,5]
counts = defaultdict(int)

for n in nums:
    counts[n]+=1
print(counts)

from collections import Counter
nums = [1,1,2,4,3,4,3,2,4,2,5,6]
counts = Counter(nums)
print(counts)
