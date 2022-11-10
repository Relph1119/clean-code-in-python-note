#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: unittest_merge_request.py
@time: 2022/11/10 17:33
@project: clean-code-in-python-note
@desc: P232 使用unittest测试
"""
import unittest

from ch08.merge_request import MergeRequest, MergeRequestStatus, MergeRequestException, AcceptanceThreshold


class TestMergeRequestStatus(unittest.TestCase):

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvote("maintainer")
        self.assertEqual(merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_created_is_pending(self):
        self.assertEqual(MergeRequest().status, MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(merge_request.status, MergeRequestStatus.PENDING)

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")
        self.assertEqual(merge_request.status, MergeRequestStatus.APPROVED)

    def test_cannot_upvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaises(MergeRequestException, merge_request.upvote, "dev1")

    def test_cannot_downvote_on_closed_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            merge_request.downvote,
            "dev1"
        )


class TestAcceptanceThreshold(unittest.TestCase):
    def setUp(self) -> None:
        """
        在测试之前运行的代码
        :return:
        """
        self.fixture_data = (
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
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)
