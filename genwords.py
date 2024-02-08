import random

class FileGenerator:
    def __init__(
            self,
            output_file: str,
            split: int = 1
        ):
        self.output_file = output_file
        self.split = split

    def generate_random_string(
            self,
            chars: str,
            number_of_words: int,
            min_size: int,
            max_size: int
    ):
        words = []
        for _ in range(number_of_words):
            word_length = random.randint(min_size, max_size)
            word = ''.join(random.choices(chars, k=word_length))
            words.append(word)

        return ' '.join(words)

    def write_to_files(
            self,
            chars: str = 'abcdefghijklmnopqrstuvwxyz',
            number_of_words: int = 100,
            min_size: int = 3,
            max_size: int = 10
    ):
        for i in range(self.split):
            filename = self.output_file + str(i)
            file = open(filename, "w")
            file.write(
                self.generate_random_string(
                    chars=chars,
                    number_of_words=number_of_words,
                    min_size=min_size,
                    max_size=max_size
                )
            )
