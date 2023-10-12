from checkout import checkout, get_hash

folder_in = "/home/user/fld_in/"
folder_out = "/home/user/fld_out/"
folder_fld = "/home/user/fld/"


def test_step_one():
    # test1
    assert checkout(f"cd {folder_in}; 7z a {folder_out}arch", "Everything is Ok"), "test1 FAIL"


def test_step_two():
    # test2
    assert checkout(f"cd {folder_out}; 7z d ./arch.7z file1", "Everything is Ok"), "test2 FAIL"


def test_step_three():
    # test3
    assert checkout(f"cd {folder_out}; 7z l ./arch.7z", "Name"), "test3 FAIL"


def test_step_four():
    # test3
    assert checkout(f"cd {folder_out}; 7z x ./arch.7z", "Everything is Ok"), "test4 FAIL"


def test_step_five():
    res1 = checkout(f"cd {folder_in}; 7z h file2", "Everything is Ok")
    hs = get_hash(f"cd {folder_in}; crc32 file2".upper())
    res2 = checkout(f"cd {folder_in}; 7z h file2", hs)
    assert res1 and res2, "test5 FAIL"