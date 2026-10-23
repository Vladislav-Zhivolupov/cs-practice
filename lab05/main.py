#main
import os

from logstats import count_levels, top_errors, format_report

path = input('введите events.log > ')

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

total = sum(counts.values())
print(total)
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.txt")
with open(report_path, "w", encoding="utf-8") as report:
    report.write(format_report(counts, errors))
