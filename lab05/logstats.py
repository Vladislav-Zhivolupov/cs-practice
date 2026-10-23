#logstats
LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]


def parse_event(line):

    parts = line.strip().split(None, 2)
    if len(parts) < 3:
        raise ValueError("в строке меньше трёх частей: " + line)

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError("неизвестный уровень: " + level)

    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    messages = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            message = event["message"]
            messages[message] = messages.get(message, 0) + 1

    pairs = []
    for message in messages:
        pairs.append([message, messages[message]])

    pairs.sort(key=lambda pair: (-pair[1], pair[0]))
    return pairs[:n]


def format_report(counts, errors):
    text = "Отчёт по журналу\n\n"

    for level in sorted(counts):
        text += level + ": " + str(counts[level]) + "\n"

    text += "\nЧастые ошибки:\n"
    for message, count in errors:
        text += "- " + message + " — " + str(count) + "\n"

    return text
