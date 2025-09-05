from builder_design_pattern.example_one.concrete.builders.small_house_builder import SmallHouseBuilder
from builder_design_pattern.example_one.concrete.builders.big_house_builder import BigHouseBuilder
from builder_design_pattern.example_one.concrete.director import HouseDirector

def main():
    small_house_builder = SmallHouseBuilder()
    big_house_builder = BigHouseBuilder()

    house_director = HouseDirector()
    
    # Small house with custom name
    house_director.builder = small_house_builder 
    small_house = house_director.construct_house("My Cozy Home")
    print(f"Small House: {small_house}")
    
    # Big house with custom name
    house_director.builder = big_house_builder
    big_house = house_director.construct_house("Luxury Mansion")
    print(f"Big House: {big_house}")
    
    # Direct builder usage (without director)
    custom_small_house = (SmallHouseBuilder()
                         .set_floors()
                         .set_walls()
                         .set_house_name("Custom Small House")
                         .house)
    print("Custom Small House:")
    print(custom_small_house)

if __name__ == "__main__":
    main()