random_list = [3.1, 2.7, 5.5, 107, 73, 41, 'hello', 'python', 'world', 'AI']

data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

def map_int_to_dict(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int_mapped = list(map(map_int_to_dict, data_int))

print("data float:", data_float)
print("data int:")
for item in data_int_mapped:
    print(item)
print("data string:", data_string)