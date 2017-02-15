import time

input("press enter and then count 20 seconds")
start = time.time()

input("After 20 seconds, press enter again")
end = time.time()

et = end - start
print("real time :", et)
print("difference :", abs(et - 20))
