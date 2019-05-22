def min_edit_distance(source, target, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if source[m-1] == target[n-1]:
        return min_edit_distance(source, target, m-1, n-1)

    return 1 + min( min_edit_distance(source, target, m, n-1),
                    min_edit_distance(source, target, m-1, n),
                    min_edit_distance(source, target, m-1, n-1))





source = ""
target = "hellow"
print(min_edit_distance(source, target, len(source), len(target)))