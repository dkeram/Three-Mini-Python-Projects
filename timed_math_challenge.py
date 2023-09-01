import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


input('Press ente to start!')
print('--------------------')

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(print(f'Problem # {i+1}: {expr} = '))
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('--------------------')
print(f'Nice work! You finished in {total_time} seconds!')