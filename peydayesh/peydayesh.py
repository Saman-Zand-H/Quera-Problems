def find(num1, num2, num3):
    main_ls = [1, 2, 3, 4]
    ls = [num1, num2, num3]
    return [*filter(lambda i: i not in ls, main_ls)][0]