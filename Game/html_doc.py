class Tag:

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)

    def add_tag(self, name, contents):
        self.new_tag = Tag(name, contents)

class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  #Doc type doesnt have end tag

class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self.head_contents = []

    def add_tag(self, name, contents):
        super().add_tag(name, contents)
        self.head_contents.append(self.new_tag)

    def display(self, file=None):
        for tag in self.head_contents:
            self.contents += str(tag)

        super().display(file=file)

class Body(Tag):

    def __init__(self):
        super(Body, self).__init__('body', '')  # body contents will be built seperate
        self.body_contents = []

    def add_tag(self, name, contents):
        super().add_tag(name, contents)
        self.body_contents.append(self.new_tag)

    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)

        super().display(file=file)

class HtmlDoc:

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_head_tag(self, name, contents):
        self._head.add_tag(name, contents)

    def add_body_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_head_tag('title', 'Document Title')
    my_page.add_body_tag('h1', 'Main heading')
    my_page.add_body_tag('h2', 'sub-heading')
    my_page.add_body_tag('p', 'This is a paragraph')
    with open('test.html', 'w') as test_doc:
        my_page.display(file=test_doc)
    print(my_page._head.head_contents)