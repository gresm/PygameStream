from typing import Optional, Union, Tuple, Sequence, List
import pygame as pg
# noinspection PyUnresolvedReferences
from pygame.display import *


class __DisplaySurface:
    def __init__(self, size: Optional[Union[Tuple[int, int], Sequence[int]]],
                 flags: Optional[int] = 0,
                 depth: Optional[int] = 0,
                 display: Optional[int] = 0,
                 vsync: Optional[int] = 0):
        self.vsync = vsync
        self.display = display
        self.depth = depth
        self.flags = flags
        self.size = size
        self.__current: int = 0
        self.__screens: List[pg.Surface] = [pg.Surface(size, flags, depth), pg.Surface(size, flags, depth)]

    @property
    def __display(self):
        return self.__screens[self.__current]

    def __instancecheck__(self, instance: Union["__DisplaySurface", pg.Surface]):
        if super(self.__class__, self).__instancecheck__(instance):
            return True
        return isinstance(instance, pg.Surface)


__real_surface: __DisplaySurface = ...


def set_mode(
        size: Optional[Union[Tuple[int, int], Sequence[int]]],
        flags: Optional[int] = 0,
        depth: Optional[int] = 0,
        display: Optional[int] = 0,
        vsync: Optional[int] = 0
) -> __DisplaySurface:
    global __real_surface
    ret = __DisplaySurface(size, flags, depth, display, vsync)
    __real_surface = ret
    return ret
