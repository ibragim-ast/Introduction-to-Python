def write_to_base(a):
    with open('base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a}')

def edit_base(old_string,new_string):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        a = []
        for i in base:
            a.append(i)
    a[a.index(old_string)] = new_string
    with open ('base.txt', 'w+', encoding='utf-8') as base:
        for i in a:
            base.write(f'{i}')