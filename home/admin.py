# Register your models here.

# import os
# grid = [['p','x','x','x','x','x','x','x','x',],
#         ['x','w','x','x','x','x','x','x','x',],
#         ['x','w','x','x','x','x','x','x','x',],
#         ['x','w','x','x','x','x','x','x','x',],
#         ['x','w','x','x','x','x','x','x','x',],
#         ['x','w','w','x','x','x','x','x','x',]]

# print("🐍") #protagonist

# def draw_grid():
#     os.system("cls" if os.name == "nt" else "clear")
#     for row in grid:
#         print(" ".join(row))
#     print("\nControls: WASD, Q to quit")

# running = True
# while running:
#     draw_grid()
#     move = input("Move:").lower()
#     if move == "q":
#         print("Bye!")
#         running = False
#         break
#     r, c = -1, -1

#     for row_idx, row_list in enumerate(grid):
#         if "p" in row_list:
#             r, c = row_idx, row_list.index("p")
#             break

#     new_r, new_c = r, c
#     if move == "w": new_r -= 1
#     elif move == "s": new_r += 1
#     elif move == "a": new_c -= 1
#     elif move == "d": new_c += 1
#     else: continue

#     if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
#         if grid[new_r][new_c] != "w":
#             grid[r][c] = "x"
#             grid[new_r][new_c] = "p"
#         else:
#             input("Hit a wall. Enter")
#     else:
#         input("Border reached. Enter")
