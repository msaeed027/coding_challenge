from itertools import product
from rx import Observable, from_list
from .rx.operators import cartesian_product


class Combination:

    @staticmethod
    def py_combine(lists: list) -> list:
        """"
        Get cartesian product of input lists using python built-in itertools.product

        :param lists: list of lists
        :return: Cartesian product of inputted lists (all possible combination between inputted lists)
        """
        return [combined_values for combined_values in product(*lists)]

    @staticmethod
    def custom_combine(lists: list) -> list:
        """"
        Get cartesian product of input lists using custom algorithm

        :param lists: list of lists
        :return: Cartesian product of inputted lists (all possible combination between inputted lists)
        """
        result = [[]]
        for pool in lists:
            result = [x+[y] for x in result for y in pool]
        return result

    @staticmethod
    def rx_combine(lists: list) -> list:
        """"
        Get cartesian product of input lists using reactive programming

        :param lists: list of lists
        :return: Cartesian product of inputted lists (all possible combination between inputted lists)
        """
        source = from_list(lists)

        output_stream = source.pipe(
            cartesian_product()
        )

        return Combination.observable_to_list(output_stream)

    @staticmethod
    def observable_to_list(observable: Observable) -> list:
        res = []

        def on_next(_list):
            nonlocal res
            res += [_list]

        def on_error():
            nonlocal res
            res = []

        observable.subscribe(on_next=on_next, on_error=on_error)

        return res
