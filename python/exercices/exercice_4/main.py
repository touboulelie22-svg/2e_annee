from pathlib import Path
from dataclasses import dataclass
from datetime import datetime
import csv
from math import prod


class FileIdentity:
    def __init__(self, name: str, extension: str, mime: str) -> None:
        self.name = name
        self.extension = extension
        self.mime = mime

class FileMetadata:
    def __init__(self, owner: str, created_at: datetime, updated_at: datetime) -> None:
        self.owner = owner
        self.created_at = created_at
        self.updated_at = updated_at

    def touch(self) -> None:
        self.updated_at = datetime.now()


class BaseFile:
    def __init__(self, path: Path, identity: FileIdentity, metadata: FileMetadata) -> None:
        self.path = path
        self.identity = identity
        self.metadata = metadata

    def load(self):
        raise NotImplementedError

    def save(self, data) -> None:
        raise NotImplementedError

    def summary(self) -> str:
        raise NotImplementedError

    def size(self) -> int:
        try:
            return self.path.stat().st_size
        except FileNotFoundError:
            return 0



class TextFile(BaseFile):
    def __init__(self, path: Path, identity: FileIdentity, metadata: FileMetadata, encoding: str = "utf-8") -> None:
        super().__init__(path, identity, metadata)
        self.encoding = encoding

    def load(self) -> str:
        with self.path.open("r", encoding=self.encoding) as f:
            return f.read()

    def save(self, data: str) -> None:
        with self.path.open("w", encoding=self.encoding) as f:
            f.write(data)
        self.metadata.touch()

    def summary(self) -> str:
        head = ""
        try:
            head = self.load().splitlines()[:3]
            head = " / ".join(head) if head else ""
        except FileNotFoundError:
            head = "(absent)"
        return f"[TXT] {self.identity.name}.{self.identity.extension} — owner={self.metadata.owner} — head={head}"


class CsvFile(BaseFile):
    def __init__(self, path: Path, identity: FileIdentity, metadata: FileMetadata, delimiter: str = ",") -> None:
        super().__init__(path, identity, metadata)
        self.delimiter = delimiter

    def load(self) -> list[list[str]]:
        with self.path.open("r", newline="", encoding="utf-8") as f:
            return [row for row in csv.reader(f, delimiter=self.delimiter)]

    def save(self, data) -> None:
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=self.delimiter, lineterminator="\n")
            for row in data:
                writer.writerow(list(row))
        self.metadata.touch()

    def summary(self) -> str:
        try:
            rows = self.load()
            n_rows = len(rows)
            n_cols = len(rows[0]) if rows else 0
        except FileNotFoundError:
            n_rows, n_cols = 0, 0
        return f"[CSV] {self.identity.name}.{self.identity.extension} — owner={self.metadata.owner} — shape=({n_rows}, {n_cols})"


class ImageFile(BaseFile):
    def __init__(self, path: Path, identity: FileIdentity, metadata: FileMetadata, width: int | None = None, height: int | None = None) -> None:
        super().__init__(path, identity, metadata)
        self.width = width
        self.height = height

    def load(self) -> bytes:
        with self.path.open("rb") as f:
            return f.read()

    def save(self, data: bytes) -> None:
        with self.path.open("wb") as f:
            f.write(data)
        self.metadata.touch()

    def summary(self) -> str:
        dims = f"{self.width}x{self.height}" if self.width and self.height else "unknown"
        return f"[IMG] {self.identity.name}.{self.identity.extension} — owner={self.metadata.owner} — dims={dims}"


class FileRepository:
    def __init__(self) -> None:
        self._files: list[BaseFile] = []

    def add(self, f: BaseFile) -> None:
        self._files.append(f)

    def all(self) -> list[BaseFile]:
        return list(self._files)

    def by_author(self, owner: str) -> list[BaseFile]:
        return [f for f in self._files if f.metadata.owner == owner]

    def total_size(self) -> int:
        return sum(f.size() for f in self._files)

    def summary(self) -> str:
        lines = [f.summary() for f in self._files]
        return "\n".join(lines)

base = Path("./data")
base.mkdir(exist_ok=True)

id_txt = FileIdentity(name="readme", extension="txt", mime="text/plain")
id_csv = FileIdentity(name="users", extension="csv", mime="text/csv")
id_img = FileIdentity(name="logo", extension="png", mime="image/png")

meta_alice = FileMetadata(owner="alice", created_at=datetime.now(), updated_at=datetime.now())
meta_bob = FileMetadata(owner="bob", created_at=datetime.now(), updated_at=datetime.now())

txt = TextFile(base / f"{id_txt.name}.{id_txt.extension}", id_txt, meta_alice)
csvf = CsvFile(base / f"{id_csv.name}.{id_csv.extension}", id_csv, meta_bob, delimiter=";")
img = ImageFile(base / f"{id_img.name}.{id_img.extension}", id_img, meta_alice, width=256, height=256)

txt.save("Bienvenue\nÀ bord\nDu projet")
csvf.save([["prenom", "nom"], ["John", "Doe"], ["Emma", "Smith"]])
img.save(b"\x89PNG\r\n\x1a\n...")  # octets factices

repo = FileRepository()
repo.add(txt)
repo.add(csvf)
repo.add(img)

print(repo.summary())
print("Total size:", repo.total_size())
for f in repo.by_author("alice"):
    print("Owner alice ->", f.identity.extension, "updated_at:", f.metadata.updated_at)