def test_2_wei_bag_problem1(bag_size, weight, value):
    """
    :param bag_size: 整数，背包容量
    :param weight: list，元素为各物品重量，顺序
    :param value: list，元素为各物品价值，顺序
    :return:
    """
    rows, cols = len(weight), bag_size + 1
    # 先创建 rows行 cols列 值全部为0的空白表格
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # 初始化dp数组
    for i in range(rows):
        dp[i][0] = 0
        # 背包容量为0时，所有行的第一列价值为0

    first_item_weight, first_item_value = weight[0], value[0]
    for j in range(1, cols):
        if first_item_weight <= j:
            dp[0][j] = first_item_value
            # 第一个物品重量小于背包容量时，第一行对应格子点价值为第一个物品价值

    # 开始遍历，先物品，后背包
    for i in range(1, len(weight)):
        cur_weight, cur_value = weight[i], value[i]
        # 遍历所有物品的重量与价值
        for j in range(1, cols):
            if cur_weight > j: # 背包装不下当前物品
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_weight] + cur_value)
    print(dp)


if __name__ == "__main__":
    bag_size = 4
    weight = [1,3,4]
    value = [15,20,30]
    test_2_wei_bag_problem1(bag_size,weight,value)