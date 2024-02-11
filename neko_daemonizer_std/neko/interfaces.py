from abc import ABC, abstractmethod
from typing import Callable


class DaemonizerInterface(ABC):
    @staticmethod
    @abstractmethod
    def release_execution(
        main: Callable,
        setup: Callable = None,
        post_daemonized: Callable = None,
        pre_call: Callable = None,
    ) -> None:
        """
        Create new independent process with specified function and exit. If passed
        functions have arguments, pass lambda: func(arg) instead of func

        :param main: Function called in new released process
        :param setup: Called before release, in parent process
        :param post_daemonized: Called after release, in parent process
        :param pre_call: Called before main, in released process
        """

    @staticmethod
    @abstractmethod
    async def async_release_execution(
        main: Callable,
        setup: Callable = None,
        post_daemonized: Callable = None,
        pre_call: Callable = None,
    ) -> None:
        """
        Create new independent process with specified asynchronyous function and exit.
        If passed functions have arguments, pass lambda: async_func(arg) instead of
        async_func

        :param main: Function called in new released process
        :param setup: Called before release, in parent process
        :param post_daemonized: Called after release, in parent process
        :param pre_call: Called before main, in released process
        """


__all__ = [DaemonizerInterface]
__replacements__ = __all__
