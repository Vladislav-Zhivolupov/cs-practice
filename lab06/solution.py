#solution.py

def count_by_extension(paths: list[str]) -> dict[str, int]:
    
    result: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[-1]
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result
 
 
def deepest_path(paths: list[str]) -> str:
    
    if not paths:
        return ""
    return max(paths, key=lambda p: (p.count("/"), p))
 
 
def human_size(n_bytes: int) -> str:

    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = float(n_bytes)
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.1f} {units[index]}"
