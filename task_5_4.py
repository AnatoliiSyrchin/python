src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [src[i] for i in range(len(src)) if src[i] and i > 1 and src[i] > src[i - 1]]
print(f"{result = }")