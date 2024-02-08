from genwords import FileGenerator
from countingwords import CountingWords

if __name__ == '__main__':
    countingwords = CountingWords("input0", "output.txt")
    countingwords.map()
    countingwords.collect()
