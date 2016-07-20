def readFile(fileName, func = None):
    file = open(fileName)
    data = file.read()
    array = data.split('\n')

    def transform(str):
        if func is None:
            return str
        else:
            return func(str)

    array = map(transform, array)
    return array