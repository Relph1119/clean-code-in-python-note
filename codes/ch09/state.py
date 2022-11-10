#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: state.py
@time: 2022/11/10 20:33
@project: clean-code-in-python-note
@desc: P278 状态模式
"""
import abc
import logging
from typing import Type

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class InvalidTransitionError(Exception):
    """Raised when trying to move to a target state from an unreachable
    Source
    state.
    """


class MergeRequestState(abc.ABC):
    def __init__(self, merge_request):
        self._merge_request = merge_request

    @abc.abstractmethod
    def open(self):
        ...

    @abc.abstractmethod
    def close(self):
        ...

    @abc.abstractmethod
    def merge(self):
        ...

    def __str__(self):
        return self.__class__.__name__


class Open(MergeRequestState):
    def open(self):
        self._merge_request.approvals = 0

    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Closed

    def merge(self):
        logger.info("merging %s", self._merge_request)
        logger.info(
            "deleting branch %s", self._merge_request.source_branch
        )
        self._merge_request.state = Merged


class Closed(MergeRequestState):
    def open(self):
        logger.info(
            "reopening closed merge request %s",
            self._merge_request
        )
        self._merge_request.state = Open

    def close(self):
        """Current state."""

    def merge(self):
        raise InvalidTransitionError("can't merge a closed request")


class Merged(MergeRequestState):
    def open(self):
        raise InvalidTransitionError("already merged request")

    def close(self):
        raise InvalidTransitionError("already merged request")

    def merge(self):
        """Current state."""


class MergeRequest:
    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state = None
        self.approvals = 0
        self.state = Open

    @property
    def state(self) -> MergeRequestState:
        return self._state

    @state.setter
    def state(self, new_state_cls: Type[MergeRequestState]):
        self._state = new_state_cls(self)

    @property
    def status(self):
        return str(self.state)

    def __getattr__(self, method):
        return getattr(self.state, method)

    def __str__(self):
        return f"{self.target_branch}:{self.source_branch}"


if __name__ == '__main__':
    mr = MergeRequest("develop", "mainline")
    mr.open()
    print("After open, approvals is", mr.approvals)

    mr.approvals = 3
    mr.close()
    print("After modify 3 and close, approvals is", mr.approvals)

    mr.open()
    mr.merge()
    mr.close()
