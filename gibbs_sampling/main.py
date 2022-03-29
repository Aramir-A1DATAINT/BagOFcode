import random 

def roll_a_die():
    # 주사위 눈은 1 ~ 6 
    # 각 눈이 선택될 확률은 동일
    return random.choice(range(1, 7))

def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1 + d2

# x에 대한 y의 조건부 확률/ y에 대한 x의 조건부 확률

def random_y_given_x(x):
    # x 값을 알고 있다는 전제 하에
    # y 값이 선택될 확률
    # y는 x+1, x+5, x+6 중 하나
    return x + roll_a_die()

def random_x_given_y(y):
    # y값을 알고 있다는 전제 하에
    # x값이 선택될 확률
    # 첫째 둘째 주사위 값의 합이 7이거나
    # 7보다 작다면
    if y <= 7:
        # 첫번째 주사위의 눈은 1~6
        # 각 눈이 선택될 확률은 동일
        return random.randrange(1, y)
    # 만약 총합이 7보다 크다면
    else:
        # 첫번째 주사위의 눈은
        # y-6, y-5,..., 6
        # 각 눈이 선택될 확률은 동일
        return random.randrange(y-6, 7)

# gibbs_sample 함수
def gibbs_sample(num_iters=100):
    # 초기값이 무엇이든 상관없음
    x, y = 1, 2
    for _ in range(num_iters):
        x = random_x_given_y(y)
        y = random_y_given_x(x)
        print(x, y)
    print(x, y)
    return x, y

'''
깁스 샘플 수를 늘려서 결합확률분포 direct_sample로부터 
뽑은 결과와 비교하면 유사한 결과가 나오는걸 확인할 수 있습니다.
다시 말해 결합확률분포를 모를 때,
이미 알고 있는 일부 조건부 확률분포에
깁스 샘플링을 적용하여 해당 결합확률분포의 
표본을 얻어낼 수 있다는 것입니다.
'''

gibbs_sample()