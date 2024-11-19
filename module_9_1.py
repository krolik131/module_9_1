def apply_all_func(int_list, *functions):
    result = dict()
    for i in range(len(functions)):
        result1 = {functions[i].__name__ : functions[i](int_list)}
        result.update(result1)
    return result

print(apply_all_func([6, 20, 15, 9], max,min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))