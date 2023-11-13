import inspect
def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        result = func(*args)
        if isinstance(result, list) or inspect.isgenerator(result):
            for el in result:
                print(el)
        elif isinstance(result, dict) :
            for key in result:
                print(key, "=", result[key])
        else:
            print(result)
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()