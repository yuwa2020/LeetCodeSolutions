class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = []

        for operation in operations:
            if operation == '+':
                number = int(result[-1]) + int(result[-2])
                result.append(number)

            elif operation == 'D':
                number = int(result[-1]) * 2
                result.append(number)

            elif operation == 'C':
                result.pop()

            else:
                result.append(int(operation))

        sum = 0
        for score in result:
            sum += int(score)
        
        return sum
        