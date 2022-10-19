import ui
import model
import writer


def start_work():
    return ui.get_user_data()


def search_work():
    user_data = ui.get_user_data('Введите данные сотрудника для поиска: \n')
    return model.search_data(user_data)


def add_data_work():
    id = ui.get_user_data('Введите id сотрудника: ')
    name = ui.get_user_data('Введите ФИО сотрудника: ')
    phone = ui.get_user_data('Введите номер телефона сотрудника: ')
    post = ui.get_user_data('Введите должность сотрудника: ')
    cost = ui.get_user_data('Введите зарплату сотрудника: ')
    return (f'{id} || {name} || {phone} || {post} || {cost}\n')


def write_to_file(a):
    writer.write_to_base(a)


def edit_work():
    old_string = search_work()
    ui.print_data(old_string)
    ui.print_data('Введите новые данные для сотрудника:')
    new_string = add_data_work()
    writer.edit_base(old_string, new_string)


while True:
    mode = int(start_work())
    if mode == 1:
        ui.print_data(search_work())
    elif mode == 2:
        write_to_file(add_data_work())
    elif mode == 3:
        edit_work()
    else:
        break
