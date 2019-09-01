print('Hello word')

i = 1
while i <= 5:
    print(i)
    i= i+1

print("Finished")
print("*********************")
words = ["Hello", "world", "1"]
print(words[0])
print(words[1])
print(words[2])
print("*********************")

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
print(nums)

try:
    nums.index(5)

except Exception:
 print('')

for num in nums:
    print(num)




