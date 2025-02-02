def sum_of_coins(coins, target):
    coins.sort(reverse=True)
    idx, used_coins = 0, {}
    
    while True:
        if target <= 0 or idx >= len(coins):
            break
        count_coins = target // coins[idx]
        target %= coins[idx]

        if count_coins > 0:
            used_coins[coins[idx]] = count_coins

        idx += 1

    if target != 0:
        return 'Error'
    else:
        result = f'Number of coins to take: {sum(used_coins.values())}\n'

        for coin, count in used_coins.items():
            result += f'{count} coin(s) with value {coin}\n'

        return result


coins = list(map(int, input().split(', ')))
target = int(input())
print(sum_of_coins(coins, target))
