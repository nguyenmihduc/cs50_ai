candidates = [
    ("up", (6 - 1, 3)),
    ("down", (6 + 1, 3)),
    ("left", (6, 3 - 1)),
    ("up", (6, 3 + 1)),
]

result = []

for action, (r, c) in candidates:
    # print(">>> action:", action)
    # print(">>> (r,c):", (r, c))
    result.append((action, (r, c)))

print(">>> result:", result)
