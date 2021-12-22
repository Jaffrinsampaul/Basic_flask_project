# def string(str1, str2):
#     string_name = "GEEKS"
#     execution_times = len(str1) + len(str2)
#     executed_time = 0
#     for element in range(0, len(str2)):
#         executed_time += 1
#         if str2[element] in list(str1):
#             print("true")
#             if executed_time == execution_times:
#                 return True
#         else:
#             return False

# print(string(input(), input()))
import random
import string


# def encode(user_string):
#     alphabets = string.ascii_lowercase
#     encrypted_string = []
#     numbers = [i for i in range(0, 10)]
#     special_char = list(string.punctuation)
#     for string_element in range(len(user_string)):
#         if user_string[string_element] in list(alphabets):
#             encode = list(alphabets).index(user_string[string_element])
#             encrypted_string.append(encode+1)
#
#         elif user_string[string_element] == " ":
#             encrypted_string.append(user_string[string_element])
#
#         elif user_string[string_element] in special_char:
#             encrypted_string.append(user_string[string_element])
#
#         elif int(user_string[string_element]) in numbers :
#             encrypted_string.append(user_string[string_element])
#
#     return "".join(map(str, encrypted_string))
#
#
# print(encode(input()))

def array_remove():
    array= ["1", "2", "E", "E", "3"]
    remove_letter = "E"
    for _ in range(len(array)):

        if remove_letter in array:
            array.remove(remove_letter)
    return ",".join(map(str, array))


print(array_remove())

random_number = [i for i in range(100)]
print(random.choice(random_number))