# Попросить пользователя ввести слова через пробел.
# Отсортировать слова по количеству символов и вывести на экран результат.
# Введенный текст: сон машина стол книга девочка
# Результат: сон стол книга машина девочка


unsorted_words = input("Enter some words: ").split()
sorted_words = []


for word in unsorted_words:
    sorted_words.append(word)
    sorted_words.sort(key=len)


print(unsorted_words)
print(sorted_words)