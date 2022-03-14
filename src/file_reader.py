def read_file(f: str) -> str:
    dataFile = open(f, "r")
    fileText = dataFile.read()
    dataFile.close()
    return fileText


def read_file_lines(f: str) -> list[str]:
    dataFile = open(f, "r")
    fileText = dataFile.readlines()
    dataFile.close()
    return fileText
