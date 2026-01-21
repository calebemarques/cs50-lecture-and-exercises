def main():

    spacecraft = {
   # "name": "James Webb Space Telescope"
    }
   # spacecraft["distance"] = 0.0000156    
    spacecraft.update({ "distance":"0.0000156","orbit":"Sun"})
    print( create_report(spacecraft) )
    


def create_report(spacecraft):
    return f"""
    ============= REPORT ============

    Name: {spacecraft.get("name", "unknown")}
    Distance : {spacecraft.get("distance", "unknown")} AU
    orbit: {spacecraft.get("orbit", "unknown")}


    ==================================
    """

if __name__ == "__main__":
    main() 
