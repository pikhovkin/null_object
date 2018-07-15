__all__ = (
    'Null',
    'json_dumper',
)


class NullObject(object):
    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '__instance', None):
            cls.__instance = super(NullObject, cls).__new__(cls, *args)

        return cls.__instance

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self

    def __setattr__(self, name, value):
        return self

    def __delattr__(self, name):
        return self

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        return self

    def __delete__(self, instance):
        return self

    def __eq__(self, other):
        return False

    __le__ = __lt__ = __gt__ = __ge__ = __eq__

    def __ne__(self, other):
        return True

    def __bool__(self):
        return False

    __nonzero__ = __bool__

    def __len__(self):
        return 0

    __length_hint__ = __len__

    def __getitem__(self, key):
        return self

    def __setitem__(self, key, value):
        return self

    __delitem__ = __getitem__

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    next = __next__

    __reversed__ = __iter__

    def __contains__(self, item):
        return False

    def __hash__(self):
        return 0

    def __repr__(self):
        return '<Null>'

    def __str__(self):
        return 'Null'

    def __unicode__(self):
        return u'Null'

    def __bytes__(self):
        return b'Null'

    def __format__(self, formatstr):
        return 'None'

    def __copy__(self):
        return self

    def __deepcopy__(self, **kwargs):
        return self

    def __pos__(self):
        return self

    __neg__ = __abs__ = __invert__ = __pos__

    def __round__(self, ndigits=None):
        return self

    def __floor__(self):
        return 0.0

    __ceil__ = __trunc__ = __floor__

    def __add__(self, other):
        return self

    __sub__ = __mul__ = __floordiv__ = __div__ = __truediv__ = __add__
    __mod__ = __pow__ = __lshift__ = __rshift__ = __and__ = __or__ = __add__
    __xor__ = __add__
    __radd__ = __rsub__ = __rmul__ = __rfloordiv__ = __rdiv__ = __add__
    __rtruediv__ = __rmod__ = __rpow__ = __rlshift__ = __rrshift__ = __add__
    __rand__ = __ror__ = __rxor__ = __add__

    def __divmod__(self, other):
        return self, self

    __rdivmod__ = __divmod__

    def __float__(self):
        return self

    __int__ = __float__


Null = NullObject()


def json_dumper(obj):
    return None if obj is Null else obj


if __name__ == '__main__':
    import json
    import math
    import pickle

    n = Null()
    n.attr = 'value'
    n.attr1.attr = 'value'
    del n.attr1
    del n.attr1.attr2.attr3['attr']
    del Null.attr1.attr2.attr3['attr']

    -n
    +n
    ~n

    n += 1024
    n -= 1024
    n *= 1024
    n /= 1024
    n &= 1024
    n |= 1024
    n ^= 1024

    kB = 1024
    kB += n
    kB = 1024
    kB -= n
    kB = 1024
    kB *= n
    kB = 1024
    kB /= n
    kB = 1024
    kB &= n
    kB = 1024
    kB |= n
    kB = 1024
    kB ^= n

    assert n[:1] is Null
    d = [n, n]
    assert d[:1][0] is Null

    assert Null() is Null
    assert Null('value') is Null
    assert Null('value', param='value') is Null
    assert round(n.m or 0, 2) == 0
    assert round(1024, n.m or 2) == 1024
    assert math.floor(n.n() or 0) == 0
    assert math.ceil(n.n() or 0) == 0
    assert math.trunc(n.n()) == 0
    assert abs(n.n) is Null
    assert (n + 1024) is Null
    assert (1024 + n) is Null
    assert (n - 1024) is Null
    assert (1024 - n) is Null
    assert (n * 1024) is Null
    assert (1024 * n) is Null
    assert (n / 1024) is Null
    assert (1024 / n) is Null
    assert (n // 1024) is Null
    assert (1024 // n) is Null
    assert (n % 1024) is Null
    assert (1024 % n) is Null
    assert divmod(n.n, 1024)[0] is Null
    assert divmod(1024, n.n)[0] is Null
    assert (n.n ** 1024) is Null
    assert (1024 ** n.n) is Null
    assert (n.n >> 1024) is Null
    assert (1024 >> n.n) is Null
    assert (n.n << 1024) is Null
    assert (1024 << n.n) is Null
    assert (n.n & 1024) is Null
    assert (1024 & n.n) is Null
    assert (n.n | 1024) is Null
    assert (1024 | n.n) is Null
    assert (n.n ^ 1024) is Null
    assert (1024 ^ n.n) is Null
    assert '{}'.format(n.o.n.e) == '{}'.format(None)
    assert n.attr() is Null
    assert n.attr.attr() is Null
    assert n.method() is Null
    assert n.m.e.t.h.o.d().method() is Null
    assert n.method('value') is Null
    assert n.method(param='value') is Null
    assert n.method('value', param='value') is Null
    assert n.attr.method() is Null
    assert n.method().attr is Null
    assert reversed(n.m()) is Null
    assert repr(n) == '<Null>'
    assert str(n.o()) == 'Null'
    assert n is Null()
    assert n.o is Null.n.e
    assert n.o is Null().n().e()
    assert n.o(1, 2, 3, Null, Null(), d=Null()).n.e(1, d=Null()) is Null()
    assert (n or 0) == 0
    assert (n or 1024) == 1024
    assert (n or True) is True
    assert (n and True) is Null
    assert (n and True) is Null
    assert (n or n().o().n().e()) is Null
    assert (n and n.o.n.e) is Null
    assert (1024 and n.o.n.e and True) is Null
    assert n.o.n().e is Null
    assert (n.o() == Null()) is False
    assert (n.o() != Null()) is True
    assert (n.o != 1024) is True
    assert (n.o == 1024) is False
    assert (n.o != Null) is True
    assert (n.o != n.e) is True
    assert isinstance(Null().n.o.n().e or {}, dict)
    assert {0: 1, '<Null>': 2, Null(): 3}[n.o.n.e()] == 3
    assert 1 not in n.objects()
    assert 2 not in n.objects()[0]
    assert 3 not in n.objects()[0]['attr']
    assert 4 not in n.objects()[0]['attr'].get('attr')
    assert 5 not in n.objects()[n.o]
    assert 6 not in n.objects()[n.o][n.e]
    assert 7 not in n.objects()[n.o][n.e].get(n.o, n.e)
    assert n not in n.objects()
    assert n not in n.objects()[0]
    assert n not in n.objects()[0]['attr']
    assert n not in n.objects()[0]['attr'].get('attr')
    assert n not in n.objects()[n.o()]
    assert n not in n.objects()[n.o()][n.e()]
    assert n not in n.objects()[n.o()][n.e()].get(n.o(), n.e())
    assert not list(filter(int, n.o()))
    assert not list(filter(lambda item: int(n.o(item)), n.e()))
    assert not list(filter(lambda item: str(n.o(item)), n.e()))
    assert not {k: v for k, v in n.o.n.e()}

    try:
        next(n.o.n.e)
        assert False
    except StopIteration:
        pass

    assert json.loads(json.dumps({'none': n.o.n.e()[0], 'yeah': 1},
                                 default=json_dumper))['none'] is None

    null = pickle.loads(pickle.dumps(n))
    if isinstance(null, NullObject):
        null = Null
    assert null is Null

    assert Null is not NullObject()
