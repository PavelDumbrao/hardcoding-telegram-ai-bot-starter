def split_text(text: str, limit: int = 3900) -> list[str]:
    if len(text) <= limit:
        return [text]
    parts = []
    current = text
    while current:
        cut = min(limit, len(current))
        if cut < len(current):
            newline = current.rfind("\n", 0, cut)
            space = current.rfind(" ", 0, cut)
            cut = max(newline, space, cut // 2)
        parts.append(current[:cut].strip())
        current = current[cut:].strip()
    return [p for p in parts if p]
