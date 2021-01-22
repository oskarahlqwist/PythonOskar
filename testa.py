n = int(input("Hur många nummer vill du skriva?: "))

nums = []
x = 0
for i in range(n):
    x = x + 1
    print("skriv nummer: ", x)
    nums.append(int(input()))

print("Summan är: ", sum(nums))