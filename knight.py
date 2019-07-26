import fileinput

lines = list(fileinput.input())
start = map(int, lines[0].strip().split(','))
end = map(int, lines[1].strip().split(','))

print(start)
print(end)

visited = {}

def visit(x, y, target_x, target_y, moves_count, board):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return
    if (x, y) in board:
        board[(x, y)] = min(board[(x, y)], moves_count)
        return
    else:
        board[(x, y)] = moves_count
    visit(x-1, y-2, target_x, target_y, moves_count + 1, board)
    visit(x+1, y-2, target_x, target_y, moves_count + 1, board)
    visit(x+2, y-1, target_x, target_y, moves_count + 1, board)
    visit(x+2, y+1, target_x, target_y, moves_count + 1, board)
    visit(x-1, y+2, target_x, target_y, moves_count + 1, board)
    visit(x+1, y+2, target_x, target_y, moves_count + 1, board)
    visit(x-2, y-1, target_x, target_y, moves_count + 1, board)
    visit(x-2, y+1, target_x, target_y, moves_count + 1, board)
    
    
visit(start[0], start[1], end[0], end[1], 1, visited)

print(visited[(start[0], start[1])])
print(visited)