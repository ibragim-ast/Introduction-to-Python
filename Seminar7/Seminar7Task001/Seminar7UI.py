import Seminar7Model
from Seminar7Logger import log_expr, log_ans


def get_expr():
    return input()

def show_res(a):
    print(a)

expression = get_expr()
log_expr(expression)
answer = Seminar7Model.evaluate_expr(expression)

log_ans(answer)
show_res(answer)


