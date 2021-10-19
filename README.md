# randomiser

A python API to generate random data from https://random-data-api.com/.


## Installation

To install, run below command:

```bash
pip install randomiser
```


## Usage

Random data generator provides some data resources you want to generate randomly, e.g. users, addresses, etc. For full available resources, check the documentation on https://random-data-api.com/documentation.

```python
from randomiser import Randomizer

# generate random user data
Randomizer(resource="users").get()

# generate 10 random user data
Randomizer(resource="users", size=10).get()
```


## Development Requirements

If you want to contribute building `randomiser`, the first step is to install the package as an editable along with required dev pakcages.

```bash
pip install -e .[dev]
```
