from typing import Tuple, Iterable
import os
import logging

from kvd import KVStore, KVStoreClient
from urllib.request import urlretrieve

EXAMPLE_DATA = "https://raw.githubusercontent.com/savingoyal/systems-assignment/main/example.data"
TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "raw.txt")


def test_local_kv():
    kvs = KVStore(EXAMPLE_DATA)

    for k, v in _get_test_set():
        assert kvs.get(k) == v

    logging.info(f"successfully tested kv local!")


def test_remote_kv():
    KVSClient = KVStore.client()

    with KVSClient(EXAMPLE_DATA) as kvs:
        for k, v in _get_test_set():
            assert kvs.get(k) == v

    logging.info(f"successfully tested kv remote!")


def test_kv_client():
    with KVStoreClient(EXAMPLE_DATA) as kvs:
        for k, v in _get_test_set():
            assert kvs.get(k) == v
    logging.info(f"successfully tested kv client!")


def _get_test_set() -> Iterable[Tuple[str, str]]:
    try:
        os.remove(TEST_DATA_PATH)
    except OSError:
        pass

    os.makedirs(os.path.dirname(TEST_DATA_PATH), exist_ok=True)
    urlretrieve(EXAMPLE_DATA, TEST_DATA_PATH)

    with open(TEST_DATA_PATH, "r", encoding="UTF-8") as f:
        for line in f:
            parts = line.split(" ")
            if len(parts) <= 1:
                raise ValueError(f"test line had unexpect parts: {line}")
            yield parts[0], " ".join(parts[1:])


if __name__ == "__main__":
    test_local_kv()
    test_remote_kv()
    test_kv_client()
