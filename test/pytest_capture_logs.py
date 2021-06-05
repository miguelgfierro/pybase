# Explanation on how to manage logs in pytest
# The fixture caplog contains the output of logging and can be queried
# Also the fixture capsys can be used to capture a print message
#
# To execute:
# $ pytest test/pytest_capture_logs.py
# 
#
# To run pytest and see the print output, add -s
# $ pytest test/pytest_capture_logs.py::test_print -s
# test/pytest_capture_logs.py This is a print
# .
# The same can be used to see the print output in the test:
# pytest test/pytest_capture_logs.py::test_print_within_test -s
# test/pytest_capture_logs.py Bazzinga!
# .
#
#
# To run pytest and see the logging output, add -o log_cli=true
# $ pytest test/pytest_capture_logs.py::test_logging -o log_cli=true
# test/pytest_capture_logs.py::test_logging 
# ---------------------------------------------------------------------------- live log call ----------------------------------------------------------------------------
# INFO     root:pytest_capture_logs.py:8 This is an INFO log
# PASSED 
#
# If you want to see the logging output, activate the logging cli and level
# $ pytest test/pytest_capture_logs.py::test_logging_within_test -o log_cli=true -o log_cli_level=INFO
# test/pytest_capture_logs.py::test_logging_within_test 
# ---------------------------------------------------------------------------- live log call ----------------------------------------------------------------------------
# INFO     root:pytest_capture_logs.py:24 Bazzinga!
# PASSED


import logging


log = logging.getLogger()


def func_logging():
    log.info("This is an INFO log")

def test_logging(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    func_logging()
    assert "This is an INFO log" in caplog.text


def test_logging_within_test():
    assert True is True
    log.info("Bazzinga!")


def func_print():
    print("This is a print")


def func_print2():
    print("This is a print")
    print("This is another print")


def test_print(capsys):
    func_print()
    captured = capsys.readouterr()
    assert "This is a print" in captured.out


def test_print2(capsys):
    func_print2()
    captured = capsys.readouterr()
    assert "This is a print" in captured.out
    assert "This is another print" in captured.out


def test_print_within_test():
    assert True is True
    print("Bazzinga!")
