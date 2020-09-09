from solutions.day09_CompareVersionNumbers import compareVersion

def test_day09_01():
    test_version1 = "0.1"
    test_version2 = "1.1"
    test_output = -1
    assert compareVersion(test_version1, test_version2) == test_output

def test_day09_02():
    test_version1 = "1.0.1"
    test_version2 = "1"
    test_output = 1
    assert compareVersion(test_version1, test_version2) == test_output

def test_day09_03():
    test_version1 = "7.5.2.4"
    test_version2 = "7.5.3"
    test_output = -1
    assert compareVersion(test_version1, test_version2) == test_output

def test_day09_04():
    test_version1 = "1.01"
    test_version2 = "1.001"
    test_output = 0
    assert compareVersion(test_version1, test_version2) == test_output

def test_day09_05():
    test_version1 = "1.0"
    test_version2 = "1.0.0"
    test_output = 0
    assert compareVersion(test_version1, test_version2) == test_output
