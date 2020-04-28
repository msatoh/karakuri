"""
OpenCV utility functions.
"""

from functools import singledispatch
import cv2

BackendError = type('BackendError', (Exception,), {})
def _is_visible(winname):
    try:
        ret = cv2.getWindowProperty(
            winname, cv2.WND_PROP_VISIBLE
        )

        if ret == -1:
            raise BackendError('Use Qt as backend to check whether window is visible or not.')

        return bool(ret)

    except cv2.error:
        return False


@singledispatch
def _make_means_break(_):
    raise TypeError(
        'Keyword argument "break_keycode" must be '
        'integer, integer sequence, character, "all" or "nothing".'
    )

@_make_means_break.register(int)
def _(break_keycode):
    return lambda key: key == break_keycode

@_make_means_break.register(str)
def _(break_keymode):
    if len(break_keymode) == 1:
        return _make_means_break(ord(break_keymode))

    if break_keymode == 'all':
        return lambda key: key != -1

    if break_keymode == 'nothing':
        return lambda key: False

    raise ValueError(
        'You can use "all" or "nothing" to specify break mode.'
    )

@_make_means_break.register(list)
@_make_means_break.register(tuple)
def _(break_keycodes):
    return lambda key: key in break_keycodes


ORD_ESCAPE = 0x1b
def closeable_imshow(winname, img, *, break_keycode=ORD_ESCAPE):
    """
    Show image window what can be closed.
    This is wrapper function of cv2.imshow.

    Parameters
    ----------
    winname : str
        Window name.
    img : np.ndarray
        Image. So its ndim must be more than one.

    break_keycode : int, character, 'all', 'nothing', sequence of integer, default 27 (ESC)
        Keys that break window thread.

        int:            You can specify an ascii code.
        character:      You can specify an ascii character.
        'all':          React any key type.
        'nothing':      Ignore any key press.
        list or tuple:  It must contains ascii codes to break window.

    Returns
    -------
    None

    Raises
    ------
    BackendError
        You must indicate Qt as backend to use this function.
    ValueError
        Although str object passed as break_keycode, that is neither 'all' nor 'nothing'.
    TypeError
        Object passed as break_keycode is improper.
    """

    means_break = _make_means_break(break_keycode)

    while True:
        cv2.imshow(winname, img)
        key = cv2.waitKey(10)

        if means_break(key):
            break
        if not _is_visible(winname):
            break

    cv2.destroyWindow(winname)
