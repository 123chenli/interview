# values是硬币的面值values=[25, 21, 10, 5, 1]
# valuescounts钱币对应的种类数
# money 找出来的总钱数
# coinsused 对应目前钱币总数i所使用的硬币数目
def coinChange(values, valuesCount, money, coinsused):
    # 遍历从1到money所有钱数的可能
    for cents in range(1, money+1):
        minCoins = cents
        # 把所有硬币的面值遍历出来和钱数做对比
        for kind in range(0, valuesCount):
            if values[kind] <= cents:
                temp = coinsused[cents-values[kind]]+1
                if temp < minCoins:
                    minCoins = temp
        coinsused[cents] = minCoins
        print('面值：{0}的最少硬币数是：{1}'.format((cents, coinsused[cents])))

