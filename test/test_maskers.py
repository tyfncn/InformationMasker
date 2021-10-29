from information_masker.maskers import alpha_numeric_masker

def test_alpha_numeric_masker():
    assert alpha_numeric_masker("tayfun can") == "XXXXXX XXX"
    assert alpha_numeric_masker("tayfun@can.guven") == "XXXXXX@XXX.XXXXX"
    assert alpha_numeric_masker("192.168.1.1") == "XXX.XXX.X.X"
