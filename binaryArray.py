# your code goes here
#t = int (input())

#a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

t = int(input())

for i in range(t):
	N  = int(input())
	A = list(map(int , input().strip().split()))[:N]

	pivot = 1
	start = -1

	for i in range(N):
		if (A[i] < pivot):
			start = start +1
			A[i], A[start] = A[start], A[i]
		
	print(*A)
