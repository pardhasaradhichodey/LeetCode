class Solution:
    def makeEqual(self, words) -> bool:
       return all(f%len(words)==0 for f in Counter(chain(*words)).values())
    