#loops - forloop and while loop

for num in range(10):print(num)

nums = [1,2,3,4,5,6,7]
for num in nums:print(num)

#conditions can be inserted in a loop
for num in nums:
    if num % 2 == 1:
        print(num)

#equivalent of that block 
eq = [num for num in nums if num % 2 == 1]
print(eq)

#a loop can can be ended if a given condition is met
for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(10):
    if num == 5:
        continue
    print(num)


#while loop 
start = 0
while(start <= 10):
    print(start)
    start += 1

nums = [1,2,3,4,5,6,7,34,5,6,3,5,6,3,25,6,7,3,25,6,7]
start = 0
while(start <= len(nums) -1):
    print(nums[start])
    start += 1
print(nums)

data = {
    "name":"dave",
    "age":1
}
dat = [{"name":"dave","age":1},{"name":"mark","age":3}]
for x in dat:
    for k, v in x.items():
        print(k, v)