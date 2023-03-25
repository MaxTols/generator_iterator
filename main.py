import types


def flat_generator(list_of_lists):
    for items in list_of_lists:
        for i in items:
            yield i


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count_1 = -1

    def __iter__(self):
        self.count_1 += 1
        self.count_2 = 0
        return self

    def __next__(self):
        if self.count_2 == len(self.list_of_list[self.count_1]):
            iter(self)
        if self.count_1 == len(self.list_of_list):
            raise StopIteration
        self.count_2 += 1
        return self.list_of_list[self.count_1][self.count_2 - 1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

    for item in FlatIterator([
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]):
        print(item)

    print('END_ITERATOR!!!')
    print('')

    test_2()

    for item in flat_generator([
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]):
        print(item)

    print('END_GENERATOR!!!')
