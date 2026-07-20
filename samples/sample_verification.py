def verify_merge(code: str):
    """
    Checks whether explicit merge parameters are used.
    """
    if "merge(" in code and "how=" in code:
        return "Good Practice"
    return "Needs Improvement"
