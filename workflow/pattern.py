def pattern(text):
    text = text.lower()
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace(",", "")
    text = text.replace(":", "")
    # .... you can add another pattern as you wish.
    return text