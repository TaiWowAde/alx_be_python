def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator,
    handling non-numeric inputs and division by zero.
    Returns a user-friendly string in every case.
    """
    # Attempt to convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Attempt the division
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Successful division
    return f"The result of the division is {result}"
