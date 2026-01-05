"""
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
Ensure only the 1st letter of the answer is capitalised.
"""

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("MONDAY")
            case 2:
                print("TUESDAY")  
            case 3:
                print("WEDNESDAY")
            case 4:
                print("THURSDAY") 
            case 5:
                print("FRIDAY") 
            case 6:
                print("SATURDAY")
            case 7:
                print("SUNDAY")   
            case _:
                print("INVALID")
Solution_instance=Solution()
Solution_instance.whichWeekDay(2)                                    

