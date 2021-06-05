# Explanation on how to manage logs in pytest
# The fixture caplog contains the stdout and can be queried
#
# To execute:
# $ pytest test/pytest_capture_logs.py
# 
# To run pytest and see the logging output
# $ pytest test/pytest_capture_logs.py -o log_cli=true



import logging


log = logging.getLogger()


def func_logging():
    log.info("This is an INFO log")


def func_print():
    print("This is a print")


def test_logging(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    func_logging()
    assert "This is an INFO log" in caplog.text


def test_print(capsys):
    func_print()
    captured = capsys.readouterr()
    assert "This is a print" in captured.out

