# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример: абв абвгд гдеёжз непшщтг -> гдеёжз непшщтг


my_text = ('Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содербващие содержащие "абв"').split()

# frag = 'абв'
# my_text2 = []



# for word in my_text:
#     if frag not in word:
#         my_text2.append(word)

# my_text2 = ' '.join(my_text2)
# print(my_text2)

lis = input("Введите текст через пробел:\n")
print(f"Исходный текст: {lis}")
n = "абв"
lst = [i for i in lis.split() if n not in i]
print(f'Результат: {" ".join(lst)}')