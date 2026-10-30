class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def backtrack(i):
            if i == len(empties):
                return True
            # pick the remaining empty cell with the fewest candidates
            best, best_mask, best_cnt = i, 0, 10
            for j in range(i, len(empties)):
                r, c = empties[j]
                mask = ~(rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]) & 511
                cnt = bin(mask).count('1')
                if cnt < best_cnt:
                    best, best_mask, best_cnt = j, mask, cnt
                    if cnt <= 1:
                        break
            if best_cnt == 0:
                return False
            empties[i], empties[best] = empties[best], empties[i]
            r, c = empties[i]
            b = (r // 3) * 3 + c // 3
            m = best_mask
            while m:
                bit = m & -m          # lowest candidate digit
                m ^= bit
                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit
                board[r][c] = str(bit.bit_length())
                if backtrack(i + 1):
                    return True
                rows[r] ^= bit        # undo and try the next digit
                cols[c] ^= bit
                boxes[b] ^= bit
            board[r][c] = '.'
            return False

        backtrack(0)