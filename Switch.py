def winter():
    print('winter')
    return


def summer():
    print('summer')
    return




def autumn():
    print('autumn')
    return


def spring():
    print('spring')
    return


def operations(season):
    weather = {'a': summer, 'b': winter, 'c': autumn, 'd': spring}
    weather[season]()


operations('a')
operations('d')
