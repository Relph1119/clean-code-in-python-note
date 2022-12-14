#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: delete_user_auth.py
@time: 2022/11/10 12:37
@project: clean-code-in-python-note
@desc: P164 禁止没有管理员权限的用户从对象中删除属性
"""


class ProtectedAttribute:
    def __init__(self, requires_role=None) -> None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, user, value):
        if value is None:
            raise ValueError(f"{self._name} can't be set to None")
        user.__dict__[self._name] = value

    def __delete__(self, user):
        if self.permission_required in user.permissions:
            user.__dict__[self._name] = None
        else:
            raise ValueError(f"User {user!s} doesn't have {self.permission_required} permission")


class User:
    """Only users with "admin" privileges can remove their email address."""
    email = ProtectedAttribute(requires_role="admin")

    def __init__(self, username: str, email: str, permission_list: list = None) -> None:
        self.username = username
        self.email = email
        self.permissions = permission_list or []

    def __str__(self):
        return self.username


if __name__ == '__main__':
    admin = User("root", "root@d.com", ["admin"])
    user = User("user", "user@d.com", ["email", "helpdesk"])
    print("the email of admin is", admin.email)
    del admin.email
    print("after delete, the email of admin is", admin.email)
