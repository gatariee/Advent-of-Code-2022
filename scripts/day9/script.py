from collections import defaultdict
def move(curr_pos, curr_move):
    return [curr_pos[0] + moves[curr_move][0], curr_pos[1] + moves[curr_move][1]]
with open('../../inputs/day9.txt', 'r') as f:
    moves = {
        'U': [0, 1],
        'D': [0, -1],
        'L': [-1, 0],
        'R': [1, 0]
        }
    visited = defaultdict(int)
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited[",".join(map(str, tail_pos))] = 1
    for row in f:
        curr_move, q = row.split(' ')
        q = int(q)
        for i in range(q):
            prev_i = head_pos[0]
            prev_j = head_pos[1]
            head_pos = move(head_pos, curr_move)
            if max(abs(head_pos[0] - tail_pos[0]), abs(head_pos[1] - tail_pos[1])) > 1:
                tail_pos = [prev_i, prev_j]
                visited[",".join(map(str, tail_pos))] = 1
print(sum(visited.values()))