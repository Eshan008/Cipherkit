def require_non_empty(text: str, field_name: str = "Input") -> None:
    if not text or not text.strip():
        raise ValueError(f"{field_name} cannot be empty.")
