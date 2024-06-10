from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    n = SecretInteger(Input(name="n", party=party1))
    fib1 = SecretInteger(0)
    fib2 = SecretInteger(1)
    i = SecretInteger(2)  # Start from the third term
    while i <= n:
        new_fib = fib1 + fib2
        fib1 = fib2
        fib2 = new_fib
        i = i + SecretInteger(1)
    return [Output(fib2, "fibonacci_output", party=party1)]