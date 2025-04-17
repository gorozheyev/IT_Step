def shortest_path_with_wall_break(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Находим старт и конец
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)

    # visited[x][y][b] — посещали ли (x, y), где b = 0 если стену не ломали, 1 — если ломали
    visited = [[[False, False] for _ in range(cols)] for _ in range(rows)]
    queue = []

    # Старт: координаты, длина пути, использовали ли разрушение стены
    queue.append((start[0], start[1], 0, False))  # x, y, distance, wall_broken
    visited[start[0]][start[1]][0] = True

    while queue:
        x, y, dist, wall_broken = queue.pop(0)

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                cell = maze[nx][ny]

                if (cell == 0 or cell == 'E') and not visited[nx][ny][int(wall_broken)]:
                    visited[nx][ny][int(wall_broken)] = True
                    queue.append((nx, ny, dist + 1, wall_broken))

                elif cell == 1 and not wall_broken and not visited[nx][ny][1]:
                    # Разрушаем стену
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, True))

    return -1  # если пути нет


# Пример:
maze = [
    ['S', 0, 1, 0, 'E'],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(shortest_path_with_wall_break(maze))
