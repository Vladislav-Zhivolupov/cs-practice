#formats

import json
import re


def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    header = [name.strip() for name in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [value.strip() for value in line.split(",")]
        records.append(dict(zip(header, values)))
    return records


def _convert_value(raw: str):

    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if re.fullmatch(r"-?\d+\.\d+", raw):
        return float(raw)
    if raw.lower() in ("true", "yes"):
        return True
    if raw.lower() in ("false", "no"):
        return False
    return raw


def parse_settings(lines: list[str]) -> dict:

    settings: dict = {}
    current_list = None
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line == "-" or line.startswith("- "):
            if current_list is not None:
                current_list.append(_convert_value(line[1:].strip()))
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list = []
            settings[key] = current_list
        else:
            current_list = None
            settings[key] = _convert_value(value)
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:

    merged = []
    for row in rows:
        additions = extra.get(row.get(key), {})
        merged.append({**additions, **row})
    return merged


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
