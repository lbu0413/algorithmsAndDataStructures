

def coin_change(n, coins):
    count = 0

    for coin in coins:
        count += n // coin
        n %= coin

    return count


n = 1260
coins = [500, 100, 50, 10]
# 큰 단위의 화폐부터 차례대로 확인
print(coin_change(n, coins))
