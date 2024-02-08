from abc import ABC, abstractmethod
from collections.abc import Iterable

class MapReduce(ABC):
    def __init__(self, input_name, output_name):
        self.input = input_name
        self.output = output_name
        self.input_file = None
        self.output_file_tmp = None
    
    def open_input(self):
        self.input_file = open(self.input, "r")

    def close_input(self):
        self.input_file.close()
    
    def close_output_tmp(self):
        if self.output_file_tmp:
            self.output_file_tmp.close()

    @property
    def input_content(self):
        if not self.input_file:
            self.open_input()

        return self.input_file.read()

    def emit_intermediate(self, key: str, value):
        if not self.output_file_tmp:
            self.output_file_tmp = open(self.output + ".tmp", "a")

        text = f"{key} {str(value)}\n"
        self.output_file_tmp.write(text)

    def emit(self, key: str, value):
        if not self.output_file:
            self.output_file = open(self.output, "a")

        text = ' '.join([key, str(value)])
        self.output_file.write(text)

    def collect(self):
        mapper = {}
        tmp_file = open(self.output + ".tmp", "r")
        for line in tmp_file:
            [key, value] = line.strip().split(" ", 1)
            if mapper.get(key) is not None:
                mapper[key].append(value)
            else:
                mapper[key] = [value]

        self.mapper = mapper

    @abstractmethod
    def map(self, key: str, value: str):
        pass

    @abstractmethod
    def reduce(self, key: str, values: Iterable):
        pass
