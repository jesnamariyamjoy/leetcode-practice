class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        row_masks = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                bit = 1 << (seat - 2)  # seat2 -> bit0, ..., seat9 -> bit7
                row_masks[row] = row_masks.get(row, 0) | bit

        A = 0b00001111  # seats 2-5
        B = 0b00111100  # seats 4-7
        C = 0b11110000  # seats 6-9

        count = 2 * (n - len(row_masks))

        for mask in row_masks.values():
            if (mask & A) == 0 and (mask & C) == 0:
                count += 2
            elif (mask & A) == 0 or (mask & B) == 0 or (mask & C) == 0:
                count += 1

        return count