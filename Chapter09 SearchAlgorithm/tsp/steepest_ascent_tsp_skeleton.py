import random
import math

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, table)

    # # Call the search algorithm
    # # SteepestAscent 알고리즘을 실행하여 solution을 구하기
    solution, minimum = steepestAscent(p)

    # # Show the problem and algorithm settings
    describeProblem(p) 
    displaySetting()

    # # Report results
    displayResult(solution, minimum)

# 파일을 불러오고 가공하기 좋게 설정함
# 도시의 갯수와 좌표들이 들어있다.
# 튜플 형태
def createProblem(): 
  
    # path_file = input('Enter the file name: ')
    # f = open(path_file, 'r')
    # path_file = input('Enter the file name: ')
    f = open('tsp30.txt', 'r')

    # First line is number of cities
    # 첫 번째 줄에는 도시의 수가 기록되어 있음
    numCities = int(f.readline())
    # 두 번째 줄 부터는 각 도시의 위치(x, y)가 기록돼 있음
    locations = []
    line = f.readline()

    while line != '':
        locations.append(eval(line))
        line = f.readline()

    f.close()
    
    # 각 도시 사이의 거리를 미리 계산해 둠 (추후 계산의 편의를 위해)
    table = calcDistanceTable(numCities, locations)

    # 출력 예시
    # numCities: 30 (정수 값)
    # locations: [(8, 31), (54, 97), (50, 50), ...] (List of tuples)
    # table: return value of calcDistanceTable
    return numCities, locations, table

# 도시 사이의 거리
def calcDistanceTable(numCities, locations):
    # 도시 사이의 거리를 미리 계산해 두어서 표로 준비
    # 직선 거리는 아래와 같은 수식을 이용해 구한다
    # dist = sqrt((x1-x2)^2 + (y1-y2)^2)
    table = []
    for i in range(numCities):
        row=[]
        for j in range(numCities):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            d = round(math.sqrt(dx**2 + dy**2), 1)
            row.append(d)
        table.append(row)

    # 출력 예시
    # table: [[0.0, 80.4487, 46.0997, ...], [80.4487, 0.0, 47.1699, ...], ...]
    # 이중 list 이고, table[i][j] 의 값은 i번쨰 도시와 j번째 도시 사이의 직선 거리를 나타냄
    return table


def steepestAscent(p):
    # Random한 초기값을 생성
    # randomInit 사용
    current = randomInit(p)
    # 초기값에 대한 함수값을 계산
    valueC = evaluate(current, p)
    
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while True:
        # mutant를 생성
        neighbors = mutants(current, p)
       
         # mutant 중 가장 좋은 solution을 선택
        best, bestValue = bestOf(neighbors, p)
        
        # best solution 업데이트
        if bestValue >= valueC:
            break
        else:
            current = best
            valueC = bestValue
        # print(valueC)  #찾는 값들을 확인해 볼 수 있음
    # Best solution과 그때의 Cost를 반환
    return current, valueC


def randomInit(p):

  # 도시의 index를 이용해 방문 순서를 정할 것이므로,
    # random한 index 순서로 생성
    # 예를들어 도시가 30개 있을 경우,
    # [5, 2, 0, 29, ..., 1] 과 같이 index의 중복이 없이 랜덤한 순서를 만든다.

    numCities = p[0]
    
    init = list(range(numCities))
    random.shuffle(init)
    
    # domain의 low, up 정보를 이용해
    # low <= value <= up 범위에 해당하는 값을 random.uniform을 통해 생성
    # list 형태로 각 변수의 초기 값을 반환
    
    return init


# 계산 값을 출력해주는 함수
def evaluate(current, p):

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

# 주변 좌표들을 설정하는 함수
def mutants(current, p):
    # inversion을 이용해 여러개의 mutant를 생성한다.
    # mutant는 도시의 수 만큼 생성하기로 하자.
    # inversion을 실시하기 위한 index 2개를 생성 후 inversion function call
    # 이 때 index 2개가 중복되지 않았는지 검사하여 각기 다른 mutant가 생성되도록 실시

    numCities = p[0]
    neighbors = []
    triedPairs = []

# 현재까지 만들어진 mutants의 수 = len(neighbors) < numCities
    while len(neighbors) < numCities:
        num1 = random.randint(0, numCities-2)
        num2 = random.randint(num1+1, numCities-1)
        # if num1 > num2:
        #     num1, num2 = num2, num1
        
        # 중복 됐으면 넘어가고, 아니면 뮤턴트 생성
        if [num1, num2] in triedPairs:
            # 중복 됐으면 continue
            continue
        else:
            # 중복 안됐으면 기록해 둔다.
            triedPairs.append([num1, num2])

        neighbors.append(inversion(current, num1, num2))

    ## 중복 제거
    # hint: triedPairs = [] 라는 list를 만들어서, [i, j]가 생성된 것을 저장 후
    # 새로 만든 [i, j] 가 이미 생성되었는지 아래 expression을 이용해 확인 가능
    # if [i, j] in triedPairs

    return neighbors


# 뒤집기 구현
def inversion(current, i, j):  ## Perform inversion
    # inversion을 이용해 mutant를 생성
    # 예시
    # current: [1, 2, 3, 4, 5]
    # i: 1, j:3
    # curCopy: [1, 4, 3, 2, 5]

    curCopy = current[:]
    ## 'current' is a list of city ids

    while i < j :
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += i
        j -= j
 
    return curCopy

def bestOf(neighbors, p):
    # neighbors 각각에 대한 evaluation을 실시하여
    # 가장 좋은 solution을 best로 선정 후 반환

    # 1. 가장 처음 sample을 best라고 가정한다.
    best = neighbors[0]
    bestValue = evaluate(best, p)
    # 2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해 둔다.
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    # 3. 모두 다 비교가 끝났으면 best를 반환한다.
    return best, bestValue

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()
