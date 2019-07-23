def sqrt2_newton(num):
    guess = num / 2 # 初始化猜测值为num的一半
    diff = guess**2 - num # f(Xn)
    while abs(diff) > 1e-6:
        guess = guess - diff/(2*guess) # 根据牛顿迭代公式Xn+1=Xn-f(Xn)/f'(Xn)计算新的猜测值
        diff = guess**2 - num # 更新f(Xn)
    return guess
