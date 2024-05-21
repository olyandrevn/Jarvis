from ctypes import *
from contextlib import contextmanager

# Define our error handler type
JACK_ERROR_HANDLER_FUNC = CFUNCTYPE(None)
ALSA_ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_jack_error_handler():
    pass

def py_alsa_error_handler(filename, line, function, err, fmt):
    pass


jack_c_error_handler = JACK_ERROR_HANDLER_FUNC(py_jack_error_handler)
alsa_c_error_handler = ALSA_ERROR_HANDLER_FUNC(py_alsa_error_handler)


@contextmanager
def nojackerr():
    jack = cdll.LoadLibrary('libjack.so.0')
    # Set error handler
    jack.jack_set_error_function(jack_c_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(alsa_c_error_handler)
    #yield
    #asound.snd_lib_error_set_handler(None)


