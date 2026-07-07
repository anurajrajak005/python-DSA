#code 1
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams=dict()
    for s in strs:
        if tuple(sorted(s)) not in  anagrams:
                anagrams[tuple(sorted(s))]=[]
        anagrams[tuple(sorted(s))].append(s)
    result = []
    for key , value in  anagrams.items():
        result.append(value)
    return result

# code 2  using defaultdict
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams=defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    result = []
    for key , value in  anagrams.items():
        result.append(value)
    return result
