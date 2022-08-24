from collections import namedtuple
from unicodedata import name


DataIngestionArtifact = namedtuple(
    "DataIngestionArtifact",
    ["train_file_path","test_file_path","is_ingested","message"]
    )