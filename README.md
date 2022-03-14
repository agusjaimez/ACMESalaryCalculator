# ACMESalaryCalculator
This a Python project created to calculate the salary of ACME employees. Requested by ioet
## Project overview
Given a file this code extacts the name of each worker and the days with its worked hours. Then it uses this data to create worker objects using the Worker class which contains methods that are used to calculate the salary. Worker class also provides a __str__ method which provides the worker name and the payment that he or she should recieve.
Object oriented programming was used to develop this code
## Data file required Structure
The file should contain one or more datasets and each set should be in a line
### Example:
```
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
```
## Run Instructions
Run main.py using Python3  
An example data file is provided in source folder, in case you want to use another here is what you should do:  
1. Add your data file to the resources folder
2. Run verify data_sets test
3. If the test was passed then edit the main() function and change only the file name for your file name like shown:  
```python
def main() -> None:
    dataSets = getDataSets(readFile("./resources/yourFileName.txt")) 
```
5. If the test did not pass verify your data file and repeat
