import numpy as np
from datarate_selector import select_datarate


def test_select_datarate_returns_valid_datarates():
    for i in range(1000):
        selected_datarate = select_datarate(i)
        assert selected_datarate >= 0
        assert selected_datarate <= 5


def test_select_datarate_favors_low_SF():
    datarates = np.array([select_datarate(i) for i in range(1000)])
    dr_count = np.bincount(datarates)
    assert (dr_count > 0).all()
    assert dr_count[5] >= 2 * (dr_count[4] - 1)
    assert dr_count[4] >= 2 * (dr_count[3] - 1)
    assert dr_count[3] >= 2 * (dr_count[2] - 1)
    assert dr_count[2] >= 2 * (dr_count[1] - 1)
    assert dr_count[1] >= 2 * (dr_count[0] - 1)
