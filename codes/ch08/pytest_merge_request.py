#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: pytest_merge_request.py
@time: 2022/11/10 18:04
@project: clean-code-in-python-note
@desc: P236 使用pytest测试
"""
import pytest

from ch08.merge_request import MergeRequest, MergeRequestStatus, MergeRequestException, AcceptanceThreshold


def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestStatus.REJECTED


def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_invalid_types():
    merge_request = MergeRequest()
    pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})


def test_approved():
    merge_request = MergeRequest()
    merge_request.upvote("dev1")
    merge_request.upvote("dev2")
    assert merge_request.status == MergeRequestStatus.APPROVED


def test_cannot_upvote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
    with pytest.raises(
            MergeRequestException,
            match="can't vote on a closed merge request",
    ):
        merge_request.downvote("dev1")


@pytest.mark.parametrize("context, expected_status", (
        (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING
        ),
        (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING
        ),
        (
                {"downvotes": "dev1", "upvotes": set()},
                MergeRequestStatus.REJECTED
        ),
        (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED
        ),
), )
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status
