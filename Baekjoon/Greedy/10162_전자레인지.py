time = int(input())
a = 5*60
b = 1*60
c = 10

buttons = [a, b, c]
nums = []

for idx in range(len(buttons)):
  nums.append(int(time/buttons[idx]))
  time %= buttons[idx]

if(time != 0):
  print(-1)
else:
  #print(" ".join(map(str, nums))
  print("{0} {1} {2}".format(nums[0], nums[1], nums[2]))