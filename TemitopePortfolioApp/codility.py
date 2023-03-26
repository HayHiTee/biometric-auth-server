import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag
        self.tags = {}
        self.process()
        self.check_tag_validity()

    def process(self):
        for x in self._data["items"]:
            if "tags" in x:
                for t in x["tags"]:
                    if t in self.tags:
                        self.tags[t].append(x)
                    else:
                        self.tags[t] = [x]
            else:
                raise StopIteration

    def check_tag_validity(self):
        if self.query not in self.tags or not self._data:
            raise StopIteration

    def search(self):
        for q in self.tags[self.query]:
            yield q

    def first(self):
        return self.tags[self.query][0]


if __name__ == "__main__":
    search_1 = SearchByTag('movies.json', '90s')
    print(search_1.search())
    print(search_1.first())
