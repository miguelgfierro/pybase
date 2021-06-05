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


def test_print(caplog):
    caplog.clear()
    func_print()
    assert "This is a print" in caplog.text

