from information_masker.statistics import SimpleStatistics


def test_init():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    assert "col1" in obj.columns
    assert "col2" in obj.columns
    assert "col3" in obj.columns


def test_avg():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    obj.process("col1",10)
    obj.process("col1",20)
    obj.process("col1",30)
    assert obj.get_average("col1") == 20

def test_min():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    obj.process("col1",10)
    obj.process("col1",20)
    obj.process("col1",30)
    assert obj.columns["col1"]["min"] == 10

def test_max():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    obj.process("col1",10)
    obj.process("col1",20)
    obj.process("col1",30)
    assert obj.columns["col1"]["max"] == 30

def test_sum():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    obj.process("col1",10)
    obj.process("col1",20)
    obj.process("col1",30)
    assert obj.columns["col1"]["sum"] == 60

def test_count():
    obj = SimpleStatistics(["col1", "col2", "col3"])
    obj.process("col1",10)
    obj.process("col1",20)
    obj.process("col1",30)
    obj.process("col1","NaN")
    assert obj.columns["col1"]["count"] == 3
