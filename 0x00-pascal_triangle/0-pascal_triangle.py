def pascal_triangle(n):
    """Creats Pascal's triangle upto the `n`th level

        Args:
            n (number): The number of levels to show
        Returns:
            A list of lists of integers representing Pascal's triangle
            [] otherwise
    """
    if n <= 0:
        return [];


