import sys

def main():
    coordinates_tuple = (42.3601, -71.0589)
    coordinates_list = [42.3601, -71.0589]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")








main()