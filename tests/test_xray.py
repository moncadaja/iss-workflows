import numpy as np
import pytest

from iss_workflows import xray


@pytest.mark.parametrize("k", [0.5, 3.0, 12.0])
def test_k2e_e2k_roundtrip(k):
    e0 = 8333.0
    assert xray.e2k(xray.k2e(k, e0), e0) == pytest.approx(k)


def test_k2e_is_monotonic():
    k = np.linspace(0, 15, 50)
    e = xray.k2e(k, 7112.0)
    assert np.all(np.diff(e) > 0)
    assert e[0] == pytest.approx(7112.0)
