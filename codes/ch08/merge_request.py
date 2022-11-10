#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: merge_request.py
@time: 2022/11/10 17:26
@project: clean-code-in-python-note
@desc: P231 版本控制工具的简化版，用于演示测试工具
主要功能：在合并请求中支持代码审核
1. 如果至少有一人不同意更改，合并请求将被拒绝。
2. 如果没人同意，且合并至少在另外两个开发人员看来不错，就批准它。
3. 在其他情况下，合并请求的状态将悬而未决。
"""

from enum import Enum


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"


class MergeRequestException(Exception):
    pass


class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(),
            "downvotes": set()
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        return AcceptanceThreshold(self._context).status()

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("can't vote on a closed merge request")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)

class AcceptanceThreshold:
    def __init__(self, merge_request_context: dict) -> None:
        self._context = merge_request_context

    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING
