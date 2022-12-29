import random
import math

# self => 내 자신에 대한 참조가 필요해서, 
class Problem:
    def __init__(self):
        self._solutions = None
        self._value = None
        self._numEval = None

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Tsp(Problem):
    def __init__(self):
        super().__init__()
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    def setVariables(self):
        pass
    
    def calcDistanceTable(self):
        pass

    def randomInit(self):
        pass

    def evaluate(self):
        
        # Number of evaluation을 기록하기 위해 global 변수 이용
        global NumEval
        NumEval += 1

        ## Calculate the tour cost of 'current'
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        # TSP의 비용은 총 이동한 거리의 합으로 계산한다.
        # distanceTable은 p[2]에서 제공됨
        # cost = (0번째 도시~1번째 도시 거리) + (1번째 도시~2번째 도시 거리) + ...
        
        table = p[2]
        numCities = p[0]
        cost = 0

        for i in range(numCities - 1):
            # cost += p[2][current[i]] - p[2][current[i+1]]
            cost += table[current[i]][current[i+1]]
        return cost

    def mutants(self):
        pass

    def inversion(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))

    def tenPerRow(self):
        pass


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

    def randomMutant(self):
        pass

    def describe(self):
        print()
        print("Objective function:")
        # expression 출력
        print(self._expression)   # Expression
        print("Search space:")
        # Domain 정보 출력
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i])) 

    def report(self):
       print()
       print("Solution found:")
       print(self.coordinate())  # Convert list to tuple
       print("Minimum value: {0:,.3f}".format(self._value))
       super().report()

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple
