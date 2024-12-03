from utils.helpers import *
import re

input = read_input_line(3,sep="ökasjdföalskdhg")
input = read_input_line("test_03",sep="adsflkjasdfölkjasd")

pattern = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")
res = pattern.findall(input[0])
# print(res)

tot = 0
for el in res:
    nums = list(integers(el))
    # print(nums)
    tot += nums[0]*nums[1]
print(tot)


pattern2 = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)")
matchs = pattern2.findall(input[0])

tot=0
enabled=True
for el in matchs:
    if el =="do()":
        enabled=True
    elif el =="don't()":
        enabled = False
    elif enabled:
        nums = list(integers(el))
        tot += nums[0]*nums[1]

print(tot)

