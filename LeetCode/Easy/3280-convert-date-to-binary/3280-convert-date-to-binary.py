class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        year_bin = str(bin(int(year))[2:])
        month_bin = str(bin(int(month))[2:])
        day_bin = str(bin(int(day))[2:])
        return (year_bin+'-'+month_bin+'-'+day_bin)    