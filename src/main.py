from worker import Worker
from file_reader import read_file

# This function returns the whole text in a file


def get_data_sets(text: str) -> list[str]:
    data = str(text).split("\n")
    data.remove('')
    return data


def main() -> None:
    dataSets = get_data_sets(read_file("./resources/example.txt"))
    # Create a worker for each set of data
    for data in dataSets:
        # Separate the name from the worked days and hours
        splittedData = data.split("=")
        # Create a worker with the name and the worked days and hours
        worker = Worker(splittedData[0], splittedData[1])
        print(worker.__str__())


if __name__ == "__main__":
    main()
