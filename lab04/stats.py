#stats

def parse_record(line: str) -> dict:

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city, temp, date = (p.strip() for p in parts)
    if not city:
        raise ValueError(f"пустое название города: {line!r}")
    if not date:
        raise ValueError(f"пустая дата: {line!r}")

    try:
        temperature = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError(f"температура не число: {temp!r}") from None

    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def _mean_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: total[city] / count[city] for city in total}


def average_by_city(records: list[dict]) -> dict:
    return {city: round(avg, 1) for city, avg in _mean_by_city(records).items()}


def warmest_city(records: list[dict]) -> str:
    means = _mean_by_city(records)
    if not means:
        raise ValueError("нет записей")
    return min(means, key=lambda city: (-means[city], city))




























