from problem_skeleton import Numeric
LIMIT_STUCK = 100

def main():
    # Numeric class instance를 생성한다.
    Numeric_class = Numeric()
    # setVariable을 이용해 문제를 읽어온다.
    Numeric_class.setVariables()
    # steepestAscent를 실행한다.
    firstChoice(Numeric_class)
    # describe, report를 이용해 결과를 출력한다.
    Numeric_class.describe()
    Numeric_class.report()

def firstChoice(Numeric_class):
    
    # Random한 초기값을 생성
    # randomInit 사용
    current = Numeric_class.randomInit()
    # 초기값에 대한 함수값을 계산
    valueC = Numeric_class.evaluate(current)
    i = 0
    # 계산을 반복하며 mutant를 생성후 더 나은 solution을 탐색
    while i < LIMIT_STUCK:
        successor = Numeric_class.randomMutant(current)
        valueS = Numeric_class.evaluate(successor)
        
        # best solution 업데이트
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1
    
    Numeric_class.storeResult(current, valueC)

def displaySetting(Numeric_class):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", Numeric_class.getDelta())


main()
