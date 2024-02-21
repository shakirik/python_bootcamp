def extract_full_name (names):
    return list(map(lambda n: f"{n['first']} {n['last']}", names))