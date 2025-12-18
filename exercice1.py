from pathlib import Path
from contextlib import contextmanager, ExitStack


# Partie 1 


class TempFileWriter:
    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.file = self.filepath.open("w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if self.filepath.exists():
            self.filepath.unlink()


# Exemple d'utilisation
if __name__ == "__main__":
    with TempFileWriter() as f:
        f.write("Contenu temporaire\n")



# Partie 2 — contextlib.contextmanager


@contextmanager
def temp_file():
    path = Path("temp.txt")
    f = path.open("w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        if path.exists():
            path.unlink()


with temp_file() as f:
    f.write("Autre test\n")



# Partie 3 — ExitStack


paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w", encoding="utf-8")) for p in paths]
    for f in files:
        f.write("test\n")
