def get_editor_command(editor: str) -> str:
    """

    Args:
        editor (str): Editor environment variable

    Returns:
        str: Command line for the input editor
    """

    if editor == "atom":
        return "atom -w"
    elif editor == "subl":
        return "subl -n -w"
    elif editor == "mate":
        return "mate -w"
    elif editor == "code":
        return "code"
    elif editor == "nano":
        return "nano"

    return "code"
