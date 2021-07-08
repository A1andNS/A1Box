import random


def random_num(start, end, num):
    random_result = []
    try:
        start = int(start)
        end = int(end)
        num = int(num)
        for i in range(num):
            temp = random.randint(start, end)
            random_result.append(str(temp))
        random_result_string = ' '.join(random_result)
        # print(random_result_string)
        return random_result_string
    except:
        random_result_string = "请输入整数"
        return random_result_string


if __name__ == "__main__":
    random_num(1, 2, '10')