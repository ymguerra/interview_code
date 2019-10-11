
import winsound


nums = [55, 44, 33, 22, 11, 5, 1]

greater_than_five = [i for i in nums if i > 5]

even = [i for i in nums if i % 2 == 0]

even = list(filter(lambda x: x % 2 == 0, nums))

# print(greater_than_five)
# print(even)

i = 0
while i < 10:
    winsound.PlaySound("*", winsound.SND_ALIAS)
    i + = 1
