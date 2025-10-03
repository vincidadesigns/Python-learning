print("Let's calculate the Fibonacci sequence")
n = int(input('Enter the value of n: '))
v1 = 0
v2 = 1
if n == v1:
	print('The Fibonacci value of: ',n ,'é: ',v2)
else:
	for i in range(2, n):
		fibo = v1 + v2;
		v1 = v2;
		v2 = fibo;
	print(fibo);