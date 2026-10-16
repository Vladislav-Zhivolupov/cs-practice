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














