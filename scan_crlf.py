import pathlib

root = pathlib.Path(".")

for path in root.rglob("*"):
    if path.is_file():
        try:
            data = path.read_bytes()
            if b"\r\n" in data:
                print(path)
        except Exception:
            pass
