import censusname


def generate_random_name():
    user = censusname.generate()    
    return user.split(sep=" ")


if __name__ == "__main__":
    generate_random_name()