# LINK - https://www.youtube.com/watch?v=AF8AKk9RYUQ&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=8
import time

def timer(f, *args, **kwargs):
    print("Chamou timer")

    def modificada():
        start = time.time()
        f()
        end = time.time()
        print(f'Essa função demorou {end - start} segundos')
    return modificada

@timer
def funcao1():
    print("Chamou função")
    for i in range(100_000_000):
        a = 2*20
@timer
def funcao2():
    for i in range(100_000_000):
        a = 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2

#timer(funcao1)()
funcao1()