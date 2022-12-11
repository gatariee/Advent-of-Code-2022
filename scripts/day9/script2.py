from collections import defaultdict

def move(rope, move):
    rope[0][0] += possible_moves[move][0]
    rope[0][1] += possible_moves[move][1]
    for idx in range(1, len(rope)):
        if max(abs(rope[idx - 1][0] - rope[idx][0]), abs(rope[idx - 1][1] - rope[idx][1])) > 1:
            i_diff = rope[idx - 1][0] - rope[idx][0]
            j_diff = rope[idx - 1][1] - rope[idx][1]
            i_diff = i_diff // (abs(i_diff) or 1)
            j_diff = j_diff // (abs(j_diff) or 1)
            rope[idx][0] += i_diff
            rope[idx][1] += j_diff
    return rope

possible_moves = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
}
with open('../../inputs/day9.txt', 'r') as f:
    visited = defaultdict(int)
    rope_pos = [[0, 0] for _ in range(10)]
    visited[",".join(map(str, rope_pos[0]))] = 1
    for row in f:
        move_a, q = row.split(' ')
        q = int(q)
        for i in range(q):
            rope_pos = move(rope_pos, move_a)
            visited[",".join(map(str, rope_pos[9]))] = 1
            
print(sum(visited.values()))
