import random
import math

# self => 내 자신에 대한 참조가 필요해서, 
class Problem:
    def __init__(self):
        
        self._solution = None
        self._numEval = 0
        self._minimum = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        # super를 생성해야 Problem의 변수들이 Numeric에 생긴다.
        # super 빼먹지 말것
        super().__init__()
        self._DELTA = 0.01 
        self._expression = ''
        self._domain = []

    def setVariables(self):
        # file = input('Enter the file name: ')
        # f = open('file', 'r')
        f = open('Convex.txt', 'r')
        self._expression = f.readline().rstrip()

        varNames = []
        low = []
        up = []

        line = f.readline().rstrip()
        while line != '':
            d = line.split(',')
            varNames.append(d[0])
            low.append(eval(d[1]))
            up.append(eval(d[2]))

            line = f.readline().rstrip()

        self._domain = [varNames, low, up]

    def getDelta(self):
        return self._DELTA

    def firstChoice(p):
    # Random한 초기값을 생성
    # randomInit 사용
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    i = 0
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        
        # best solution 업데이트
        if valueS > valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    
    return current, valueC

    def randomInit(self): # Return a random initial point as a list
        low, up = self._domain[1], self._domain[2]
        init = []

        for i in range(len(low)):
            init.append(random.uniform(low[i], up[i]))
        return init

    def evaluate(self, current):
        self._numEval += 1
        varName = self._domain[0] # 여기에서 변수 명을 참조

        for i in range(len(varName)):
            cmd = varName[i] + '=' + str(current[i])
            exec(cmd) # exec는 선언해서 넣는 것

        valueC = eval(self._expression)
        return valueC

    def mutants(self, current):
        neighbors = []

        for i in range(len(current)):
            m = self.mutate(current, i, self._DELTA)
            neighbors.append(m)
            m = self.mutate(current, i, -self._DELTA)
            neighbors.append(m)
        
        return neighbors
        
    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        neighbor = current[:]
        low, up = self._domain[1], self._domain[2]

        if low[i] <= neighbor[i] + d <= up[i]:
            neighbor[i] += d
            
        return neighbor 

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(p[0])   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
        low = p[1][1]
        up = p[1][2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate(self._solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._minimum))
        super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple
