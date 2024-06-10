from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    n = SecretInteger(Input(name="n", party=party1))
    factorial = SecretInteger(1)
    i = SecretInteger(1)
    while i <= n:
        factorial = factorial * i
        i = i + SecretInteger(1)
    return [Output(factorial, "factorial_output", party=party1)]