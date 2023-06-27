def pascal(n):
    if n == 1:
        print(*[1])
        return [1]
    else:
        line = [1]
        prev = pascal(n-1)
        for i in range(len(prev)-1):
            line.append(prev[i] + prev[i+1])
        line += [1]
    print(*line)
    return line
