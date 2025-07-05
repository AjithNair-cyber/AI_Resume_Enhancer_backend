def clean_json_output(text: str) -> str:
    # Remove leading/trailing markdown backticks and 'json'
    if text.strip().startswith("```json"):
        text = text.strip()[7:]  # remove ```json
    if text.strip().endswith("```"):
        text = text.strip()[:-3]  # remove trailing ```
    return text.strip()