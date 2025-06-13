class Solution:
    def fib(self, n: int) -> int:
        guardado_fibo = [0 for i in range(0,n+1)]
        if n >=1:
            guardado_fibo[1] = 1
        for i in range(2, n+1):
            first = i-1 if i- 1 > 0 else 0
            first = guardado_fibo[first]
            second = i-2 if i-2 > 0 else 0
            second = guardado_fibo[second]
            guardado_fibo[i]= first + second 
        return guardado_fibo[-1]