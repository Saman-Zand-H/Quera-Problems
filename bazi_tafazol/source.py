def game(number):
    num = [int(i) for i in str(number)]
    return max(num) - min(num)