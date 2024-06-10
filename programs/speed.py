from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    distance = SecretFloat(Input(name="distance", party=party1))
    time = SecretFloat(Input(name="time", party=party1))
    speed = distance / time
    return [Output(speed, "speed_output", party=party1)]