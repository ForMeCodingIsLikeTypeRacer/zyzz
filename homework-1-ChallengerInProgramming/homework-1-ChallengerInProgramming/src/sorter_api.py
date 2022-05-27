class Sorter:
    """Sorter Class

    A class that takes two inputs defining the sorting type and order.

    """

    sort_type = str()
    sort_order = str()

    def __init__(self, sort_type="numbers", sort_order="asc") -> None:
        """Sorter

        Args:
            sort_type (str, optional): A string describes the sorting type,
                [numbers, lexicographically]. Defaults to "numbers".
            sort_order (str, optional): A string describes the sorting order,
                (asc, desc). Defaults to "asc".

        Raises:
            ValueError: sort_type must be "numbers" or "lexicographically"
            ValueError: sort_order must be "asc" or "desc"
        """

        if sort_type.lower() not in ["numbers", "lexicographically"]:
            raise ValueError(
                'sort_type must be "numbers" or "lexicographically"')
        if sort_order.lower() not in ["asc", "desc"]:
            raise ValueError(
                'sort_order must be "asc" or "desc"')

        self.sort_type = sort_type.lower()
        self.sort_order = sort_order.lower()

    def sort_nums(self, iterable):
        """Sort an iterable of numbers

        Args:
            iterable (list, set): A list or set that contains numbers

        Raises:
            TypeError: Iterable list contains non-numbers

        Returns:
            list: Sorted list of input iterable
        """

        # Check if the whole list are numbers
        all_types = map(lambda item: isinstance(item, int), iterable)
        if False in all_types:
            raise TypeError("The iterable list contains non-numbers")

        is_desc = True if self.sort_order == "desc" else False
        return sorted(list(iterable), reverse=is_desc)

    def sort_strings(self, iterable):
        # Write your code here
        """Sort an list of strings lexicographically in asc or desc order

        Args:
            iterable (list, set): A list or set that contains strings

        Raises:
            TypeError: Iterable list contains non-strings

        Returns:
            list: Sorted list of input iterable

        """

        all_types = map(lambda item: isinstance(item, str), iterable)
        if False in all_types:
            raise TypeError("The iterable list contains non-strings")

        is_desc = True if self.sort_order == "desc" else False

        words = iterable.split()
        words.sort()
        return words




