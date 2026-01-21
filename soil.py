
def main():
      
        soil_moisture = sample()
        print(f"Soil moisture is {soil_moisture}%")


def sample ():
    import random
    return random.randint(5, 100)