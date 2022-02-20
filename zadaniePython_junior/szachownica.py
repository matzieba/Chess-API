letters_index = ["A", "B", "C", "D", "E", "F", "G", "H"]
number_index = [str(i) for i in range(1, 9)]
chessboard = []
row = []
for letter in letters_index:
    if len(row) > 0:
        chessboard.append(row)
        row = []
    for numb in number_index:
        field = letter + numb
        row.append(field)
chessboard.append(row)
