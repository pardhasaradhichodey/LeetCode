class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def min_distance(house1, house2, x, y):
            print('Entered',house1, house2)
            direct_distance = abs(house1 - house2)
            shortcut_distance = abs(house1 - x) + 1 + abs(y - house2)
            longcut_distance=abs(house2-x)+1+abs(y-house1)
            print(direct_distance, shortcut_distance,longcut_distance)
            return min(direct_distance, shortcut_distance,longcut_distance)

        result = [0] * n
        for house1 in range(1, n + 1):
            for house2 in range(house1 + 1, n + 1):
                distance = min_distance(house1, house2, x, y)
                result[distance - 1] += 2

        return result