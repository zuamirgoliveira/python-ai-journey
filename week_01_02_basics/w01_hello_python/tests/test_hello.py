from io import StringIO
from contextlib import redirect_stdout
from week_01_02_basics.w01_hello_python.hello import say_hello

def test_say_hello_output():
    buffer = StringIO()
    with redirect_stdout(buffer):
        say_hello()
    output = buffer.getvalue().strip()
    assert output == "Hello Python!"
 