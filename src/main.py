from worker import Worker

#This function returns the whole text in a file
def readFile(f: str) -> str:
    dataFile = open(f,"r")
    fileText = dataFile.read()
    return fileText

def getDataSets(text: str) -> list[str]:
    return str(text).split("\n")

def main() -> None:
    dataSets = getDataSets(readFile("./resources/example.txt")) 
    #Create a worker for each set of data
    for data in dataSets:
        #Separate the name from the worked days and hours
        splittedData = data.split("=")
        #Create a worker with the name and the worked days and hours
        worker = Worker(splittedData[0],splittedData[1])
        print(worker.__str__())

if __name__=="__main__":
    main()