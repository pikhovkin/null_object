[![CircleCI](https://img.shields.io/circleci/project/github/pikhovkin/null_object.svg)](https://circleci.com/gh/pikhovkin/null_object)
[![PyPI](https://img.shields.io/pypi/v/null-object.svg)](https://pypi.org/project/null-object/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/null-object.svg)
[![PyPI - License](https://img.shields.io/pypi/l/null-object.svg)](./LICENSE)

# null-object

Implements the null object pattern.

### Installation

    pip install null-object

### Use case

```python
import json

from null_object import Null, json_dumper


class SomeClassA(object):
    def __init__(self, name):
        self.name = name
        self.weight = 3.1415

    def pretty_name(self):
        return self.name.capitalize()


class SomeClassB(object):
    @property
    def some_obj(self):
        return a_objects.get('obj2', Null)

    def __init__(self, pk):
        self.id = pk


some_obj_a = SomeClassA('obj1')
a_objects = {
    some_obj_a.name: some_obj_a
}
some_obj_b = SomeClassB(42)
data = {
    'id': some_obj_b.id,
    'name_a': some_obj_b.some_obj.pretty_name().upper(),
    'weight': some_obj_b.some_obj.weight,
    'r_weight': round(some_obj_b.some_obj.weight or 0, 2),
    'alt_weight': (+some_obj_b.some_obj.weight - 2.71) ** 2 or 0
}
json.dumps(data, default=json_dumper)
```

### Licensing

MIT
