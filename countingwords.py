from mapreduce import MapReduce
from collections.abc import Iterable

class CountingWords(MapReduce):
    def map(self):
        content = self.input_content.split(" ")
        for word in content:
            self.emit_intermediate(word, 1)
        
        self.close_input()
        self.close_output_tmp()

    def reduce(self, key: str, values: Iterable):
        self.emit(key, len(values))
