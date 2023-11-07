class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        Magazine._all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._all_magazines

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return [article.title() for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for contributor in self._contributors:
            author_count[contributor] = author_count.get(contributor, 0) + 1
        return [author for author, count in author_count.items() if count > 2]

    def add_contributor(self, author):
        self._contributors.append(author)

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name() == name:
                return magazine
