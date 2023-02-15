# kvd
A KV store built on [ModelOS](https://github.com/aunum/modelos)

## Installation

```sh
pip install kvd
```

kvd requires a working Kubernetes cluster, found by the current kubeconfig context. Currently, it has only been tested on [KinD](https://kind.sigs.k8s.io/)

## Usage

Run locally
```python
from kvd import KVStore

EXAMPLE_DATA = "https://raw.githubusercontent.com/savingoyal/systems-assignment/main/example.data"

kvs = KVStore(EXAMPLE_DATA)

val = kvs.get("bf32dd39-9bb2-4537-ba32-9a57c90ace8")
```

Generate a remote instance on Kubernetes
```python
from kvd import KVStore

KVSClient = KVStore.client()

with KVSClient(EXAMPLE_DATA) as kvs:
    val = kvs.get("bf32dd39-9bb2-4537-ba32-9a57c90ace8")
```
> | NOTE: Remote usage requires push access to the image registry defined in `tool.modelos.image_repo` in [pyproject.toml](./pyproject.toml)

Generate remote instance on Kubernetes using only the client
```python
from kvd import KVStoreClient

with KVStoreClient(EXAMPLE_DATA) as kvs:
    val = kvs.get("bf32dd39-9bb2-4537-ba32-9a57c90ace8")
```

See [tests](./tests/store_tests.py) for working examples