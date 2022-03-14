import re
from datetime import time, datetime, date


class Worker:
    def __init__(self, name: str, work: str) -> None:
        self.name = name
        # Get each worked day with its hours saved in work variable
        self.work = work

    def get_days_and_hours(self, work: str) -> list[list[str]]:
        return re.findall(r"(\w{2})(\d{2}:\d{2})-(\d{2}:\d{2})", work)

    # This method calculates the salary of a day
    def calculate_daily_salary(
        self,
        startHour: int,
        startMinutes: int,
        finishHour: int,
        finishMinutes: int,
        day: str,
    ):
        flagIs00 = False
        # If hour equals 00:00 it breaks since this uses date.today() so finishing hour is set to 23:59
        # and a flag is raised
        if finishHour == 0 and finishMinutes == 0:
            flagIs00 = True
            finishHour = 23
            finishMinutes = 59
        # Parsing start hour and finish hour to dateTime object
        entryHour = datetime.combine(date.today(), time(startHour, startMinutes))
        exitHour = datetime.combine(date.today(), time(finishHour, finishMinutes))
        # Ranges contain the start hour, the finish hour and the billing for each hour range
        # depending on the day of the week. First Value is used for week days and second value for weekends
        ranges = [
            (
                datetime.combine(date.today(), time(0, 0)),
                datetime.combine(date.today(), time(9, 0)),
                25,
                30,
            ),
            (
                datetime.combine(date.today(), time(9, 1)),
                datetime.combine(date.today(), time(18, 0)),
                15,
                20,
            ),
            (
                datetime.combine(date.today(), time(18, 1)),
                datetime.combine(date.today(), time(23, 59)),
                20,
                25,
            ),
        ]
        dailySalary = 0
        # Calculating time worked in the day
        timeWorked = exitHour - entryHour
        # Performing an operation with datetime objects results on timedelta object so it needs to be restored
        hours, minutes = divmod(timeWorked.seconds / 60 / 60, 1)
        timeWorked = datetime.combine(
            date.today(), time(int(hours), int(round(minutes * 60)))
        )

        if day in ["MO", "TU", "WE", "TH", "FR"]:
            paymentIndex = 2
        else:  # In ["SA,SU"]
            paymentIndex = 3
        for i in range(ranges.__len__()):
            hourRange = ranges[i]
            hourlyRate = hourRange[paymentIndex]
            # If the start hour and the finish hour are both beetween the same range then this is used
            if (
                hourRange[0] <= entryHour <= hourRange[1]
                and hourRange[0] <= exitHour <= hourRange[1]
            ):
                dailySalary = (
                    timeWorked.hour * hourlyRate + (timeWorked.minute / 60) * hourlyRate
                )
            # If the start hour matches a range but the finish hour exceeds it then this is used
            elif hourRange[0] <= entryHour <= hourRange[1]:
                # Calculate how many hours do not belong to the range
                excedingHours = exitHour - hourRange[1]
                # Performing an operation with datetime objects results on timedelta object so it needs to be restored
                hours, minutes = divmod(excedingHours.seconds / 60 / 60, 1)
                excedingHours = datetime.combine(
                    date.today(), time(int(hours), round(int(minutes * 60)))
                )
                # Hours may exceed the following range as well
                if excedingHours.hour > 8:
                    # Calculating how many hours do not belong to the first two ranges
                    extraExcedingHours = excedingHours - datetime.combine(
                        date.today(), time(8, 59)
                    )
                    hours, minutes = divmod(extraExcedingHours.seconds / 60 / 60, 1)
                    extraExcedingHours = datetime.combine(
                        date.today(), time(int(hours), round(int(minutes)))
                    )
                    dailySalary = (
                        (
                            timeWorked.hour
                            + timeWorked.minute / 60
                            - excedingHours.hour
                            - excedingHours.minute / 60
                        )
                        * hourlyRate
                        + (
                            excedingHours.hour
                            + excedingHours.minute / 60
                            - extraExcedingHours.hour
                            - extraExcedingHours.minute / 60
                        )
                        * ranges[i + 1][paymentIndex]
                        + (extraExcedingHours.hour + extraExcedingHours.minute / 60)
                        * ranges[i + 2][paymentIndex]
                    )
                # In case hours only exceed the first range
                else:
                    dailySalary = (
                        timeWorked.hour
                        + timeWorked.minute / 60
                        - excedingHours.hour
                        - excedingHours.minute / 60
                    ) * hourlyRate + (
                        excedingHours.hour + excedingHours.minute / 60
                    ) * ranges[
                        i + 1
                    ][
                        paymentIndex
                    ]
        # If worker finished at 00 the code considers that he finished at 23:59,
        # thus here is added the payment for that minute
        if flagIs00 == True:
            dailySalary += 1 / 60 * ranges[2][paymentIndex]
        return dailySalary

    # This method calculates the total salary of the worker
    def calculate_salary(self):
        # Call getDaysAndHours method to retrieve work in format [["DAY","00:00"],]
        daysAndHours = self.get_days_and_hours(self.work)
        salary = 0
        for day in daysAndHours:
            # Separating minutes from hours
            startHour = day[1].split(":")
            finishHour = day[2].split(":")
            startMinutes = int(startHour[1])
            startHour = int(
                startHour[0]
            )  # Redefining variable so as not to create a new one
            finishMinutes = int(finishHour[1])
            finishHour = int(
                finishHour[0]
            )  # Redefining variable so as not to create a new one
            salary += self.calculate_daily_salary(
                startHour, startMinutes, finishHour, finishMinutes, day[0]
            )
        return salary

    def __str__(self) -> str:
        return (
            "The amount to pay "
            + self.name
            + " is: "
            + str(self.calculate_salary())
            + "USD"
        )
