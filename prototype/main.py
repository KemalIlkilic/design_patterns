from .concrete import Knight


def main():
    # Original object
    knight1 = Knight("wood", 10)
    print("Original:", knight1)

    # Cloning
    knight2 = knight1.clone()
    print("Clone:", knight2)

    # Are they the same object?
    print("Same object?", knight1 is knight2)
    print("Same values?", knight1.material == knight2.material and knight1.height == knight2.height)

    # Changing the clone does not affect the original
    knight2.material = "iron"
    knight2.height = 20
    print("Modified clone:", knight2)
    print("Original after clone modified:", knight1)


if __name__ == "__main__":
    main()