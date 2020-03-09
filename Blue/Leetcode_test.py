class Solution:
    def myAtoi(self, str = 0) -> int:
        return 0


def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            string = stringToString(line);

            ret = Solution().myAtoi(string)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()