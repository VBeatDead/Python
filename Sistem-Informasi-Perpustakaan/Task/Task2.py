random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}
float_tuple = ()
str_list = []

for item in random_list:
    if isinstance(item, int):
        int_dict[item] = (item // 100, (item % 100) // 10, item % 10)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        str_list.append (item)

print("Data integer dictionary:")
print(int_dict)
print("\nData float tuple:")
print(float_tuple)
print("\nData string list:")
print(str_list)