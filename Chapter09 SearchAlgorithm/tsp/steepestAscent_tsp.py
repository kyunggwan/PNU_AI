from problem_skeleton import Tsp

def main():
    # Numeric class instance를 생성한다.
    cls_num = Tsp()
    # setVariable을 이용해 문제를 읽어온다.
    cls_num.setVariables()
    # steepestAscent를 실행한다.
    steepestAscent(cls_num)
    # describe, report를 이용해 결과를 출력한다.
    cls_num.describe()
    cls_num.report()

def steepestAscent(cls_num):
    current = cls_num.randomInit()
    valueC = cls_num.evaluate(current)
    while True:
        neighbors = cls_num.mutants(current)
        best, bestValue = bestOf(neighbors, cls_num)

        if bestValue < valueC:
            current = best
            valueC = bestValue
        else:
            break
    cls_num.storeResult(current, valueC)

def bestOf(neighbors, cls_num):
    # p : Numeric class instance
    best = neighbors[0]
    bestValue = cls_num.evaluate(best)
    # 2. 두 번째 부터 계속 비교하면서, 더 좋은게 찾아지면 best로 저장해 둔다.
    for i in range(1, len(neighbors)):
        newValue = cls_num.evaluate(neighbors[i])
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue

    # 3. 모두 다 비교가 끝났으면 best를 반환한다.
    return best, bestValue

def displaySetting(cls_num):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", cls_num.getDelta())




main()
