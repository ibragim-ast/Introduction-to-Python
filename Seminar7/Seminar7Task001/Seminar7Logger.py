from asyncore import write


def log_expr(a):
    with open('Seminar7Data001.txt', 'w', encoding="utf-8") as f:
        f.write(f'Уравнение: {a}\n')

def log_ans(a):
    with open('Seminar7Data001.txt', 'a', encoding="utf-8") as f:
        f.write(f'Корни уровнения: {a}\n')