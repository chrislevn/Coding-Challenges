def solution(source, end):
    rowSource = source // 8
    colSource = source - (8 * (source // 8))

    rowEnd = end // 8
    colEnd = end - (8 * (end // 8))

    if rowSource == rowEnd:
        print(int(abs(end - source)))
    if colSource == colEnd:
        print(int(abs(end - source) / 8))

    if rowSource != rowEnd and colSource != colEnd:
        print((rowEnd - rowSource) + (colEnd - colSource))


solution(18, 44)
solution(19, 36)
solution(0, 1)