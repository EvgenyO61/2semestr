#Дана строка, состоящая из русских слов, набранных заглавными буквами и
#разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
#строке, заменив в нем все последующие вхождения его первой буквы на символ «.»
#(точка). Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У».
#Количество пробелов между словами не изменять.

def transform_string(input_str):
    words = input_str.split()

    transformed_words = []
    for word in words:
        if len(word) > 1:
            first_char = word[0]
            transformed_word = first_char + word[1:].replace(first_char, '.')
            transformed_words.append(transformed_word)
        else:
            transformed_words.append(word)

    result_str = ' '.join(transformed_words)
    return result_str

# Пример использования
input_string = input("Введите строку из заглавных русских слов, разделенных пробелами: ")
transformed_string = transform_string(input_string)
print("Результат преобразования:")
print(transformed_string)
