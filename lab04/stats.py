#stats

def parse_record(line: str) -> dict:

    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError(f'полей не ровно три, получено полей: {len(parts)}')

    city, temp, date = (p.strip() for p in parts)
    if (not city) or (not date):
        raise ValueError(f'город или дата пустые')

    try:
        temperature = float(temp.replace(',', '.'))
    except ValueError:
        raise ValueError(f'температура не число')


    return {'city': city, 'temperature': temperature, 'date': date}


def read_valid(lines: list[str]) -> list[dict]:

    records = []
    fir line in lines:
        if not line.strip():
            continue

        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def _mean_by_city(recordes: list[dict]) -> dict:

    total = {}
    count = {}

    for rec in recordes:
        city = rec['city']
        total[city] = total.get(city, 0.0) + rec['temperature']
        count[city] = count.get(city, 0) + 1

    return {city: total[city] / count[city] for city in total}


def average_by_city(recordes: list[dict]) -> dict:
    return {city: round(avg, 1) for city, avg in _mean_by_city(recordes).items()}


def warmest_city(recordes: list[dict]) -> str:
    means = _mean_by_city(recordes)
    if not means:
        raise ValueError('ет записей')
    return min(means, key=lambda city: (-means[city], city))































