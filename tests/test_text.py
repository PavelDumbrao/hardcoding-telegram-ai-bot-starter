from bot.services.text import split_text


def test_split_text_short() -> None:
    assert split_text("привет", 20) == ["привет"]


def test_split_text_long() -> None:
    parts = split_text("слово " * 30, 40)
    assert len(parts) > 1
    assert all(len(part) <= 40 for part in parts)
