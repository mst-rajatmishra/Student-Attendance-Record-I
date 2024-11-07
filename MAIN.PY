class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Check if a student's attendance record is eligible for an award.
        The record is eligible if it contains:
        - Less than two 'A' (Absent) records.
        - No more than two continuous 'L' (Late) records.
      
        :param s: A string representing the student's attendance record.
        :type s: str
        :return: True if the record is eligible, False otherwise.
        :rtype: bool
        """

        # Check for less than two Absents
        less_than_two_absents = s.count('A') < 2

        # Check for not having three continuous Lates
        no_three_continuous_lates = 'LLL' not in s

        # Return True if both conditions are met, otherwise False
        return less_than_two_absents and no_three_continuous_lates

# Example usage:
# creating an instance of Solution class
solution = Solution()
# invoking the checkRecord method with a sample record string
eligible = solution.checkRecord("PPALLP")  # This should return True
