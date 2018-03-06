import time
start_time = time.time()
x= 0
for i in range (1000):
	for j in range(1000):
		for k in range(10):
			x+=i+j+k
print(x)
print(time.time()- start_time)
