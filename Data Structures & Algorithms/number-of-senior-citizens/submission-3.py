class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for i in details:
            if int(i[-4:-2]) > 60:
                counter +=1
        return counter 