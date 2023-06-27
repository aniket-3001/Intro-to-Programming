n = int(input("enter paramter to print pattern: "))
for i in range(1, n+1):
    print(('*'*i)+(' '*2*(n-i))+('*'*i))
