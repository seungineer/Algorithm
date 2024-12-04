N = int(input())
cars = list(map(int, input().split()))
max_car = max(cars)
print(max_car + len(cars) - 1)