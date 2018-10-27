from server.controllers.interpolations import linear


def test_linear_interpolation_zeroth():
    linear_int = linear.Linear(x1=0.0, x2=1.0, y1=0.0, y2=255.0)
    assert linear_int.compute(x=0.5) == 127.5


def test_linear_interpolation_offset():
    linear_int = linear.Linear(x1=2.0, x2=3.0, y1=0.0, y2=1.0)
    assert linear_int.compute(x=2.5) == 0.5
