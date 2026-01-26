import time

lyrics = """Neste mundo de tantos anos
Entre tantos outros, que sorte a nossa, hein?
Entre tantas paixões
Esse encontro, nós dois, esse amor
Entre tantos outros
Entre tantos anos, que sorte a nossa, hein?
Entre tantas paixões
Esse encontro, nós dois, esse amor
Na-na, na-na-na-na-na
Na-na-na-na, na-na, na-na-na
Entre tantas paixões
Esse encontro, nós dois, esse amor
Na-na, na-na-na-na-na
Na-na-na-na, na-na, na-na-na
Na-na, na-na-na-na-na"""

lines = lyrics.split('\n')

for line in lines:
    print(line)
    time.sleep(1.9)  # Adjust the delay as needed for timing
