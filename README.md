# ACMESalaryCalculator
This a Python project created to calculate the salary of ACME employees. Requested by ioet
## Project overview
Given a file this code extacts the name of each worker and the days with its worked hours. Then it uses this data to create worker objects using the Worker class which contains methods that are used to calculate the salary. Worker class also provides a __str__ method which provides the worker name and the payment that he or she should recieve.
Object oriented programming was used to develop this code
## Data file required Structure
The file should contain one or more datasets and each set should be in a line
**IMPORTANT NOTE: File should end with an empty new line**
### Example:
```
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

```
## Run Instructions
Run main.py using Python3  
An example data file is provided in source folder, in case you want to use another here is what you should do:  
1. Add your data file to the resources folder
2. Go to testFile.py and edit the file_route attribute by changing "example.txt". Your line should like like this:
```python
file_route = "./resources/yourFileName.txt"
```
3. Run test/testFile.py to verify if your file format is correct. Use the following line to run it:
```sh
$ python3 -m unittest test.testFile.Test
```
5. If the test passed then edit the main() function located in src/main.py and change only the file name for your file name like shown:  
```python
def main() -> None:
    dataSets = getDataSets(readFile("./resources/yourFileName.txt")) 
```
5. If the test did not pass verify your data file and repeat
