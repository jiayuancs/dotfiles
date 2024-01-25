#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

__all__ = ["PROFILE_DICT"]


class ProfileBase:
    """
    ProfileBase 类用于标识 Linux 系统中一个特定工具的配置文件路径和本项目中配置文件的对应关系(每个类对应一个配置文件)。

    子类必须定义如下类属性：
        - tool_name: 工具名
        - host_filepath: 本地主机中配置文件的绝对路径
        - rep_filename: 配置文件在本仓库中的名称
    """
    # 工具的名字
    tool_name = "None"

    # Linux 主机端的一些路径配置
    host_home_path = os.getenv("HOME")  # 用户家目录
    # Linux 系统一个特定配置文件的路径(绝对路径)
    host_filepath = "None"
    # 配置文件将被备份到该目录下(绝对路径)
    host_backup_dir = os.path.join(host_home_path, ".dotfiles")

    # 当前仓库的一些路径配置
    rep_dir = "./profile"  # 对应到本仓库中配置文件所在目录
    rep_filename = "None"  # 该配置文件在本仓库rep_dir目录中的名称

    def __init__(self):
        # 配置文件对应的备份文件路径
        self.host_backup_filepath = os.path.join(self.host_backup_dir, self.rep_filename)
        # 配置文件对应的仓库路径
        self.rep_filepath = os.path.join(self.rep_dir, self.rep_filename)

    def backup(self):
        """
        将配置文件拷贝到host_backup_dir目录下
        :return: 成功时返回True，失败时返回False
        """
        return self._copy_file(self.host_filepath, self.host_backup_filepath)

    def restore(self):
        """
        将配置文件从host_backup_dir复制到原来的目录
        :return: 成功时返回True，失败时返回False
        """
        return self._copy_file(self.host_backup_filepath, self.host_filepath)

    def install(self):
        """
        用仓库中的配置文件替换host_filepath文件
        :return: 成功时返回True，失败时返回False
        """
        backup_flag = self.backup()
        if backup_flag:
            return self._copy_file(self.rep_filepath, self.host_filepath)
        else:
            print(f"SKIP: 备份失败，跳过安装 {self.tool_name} 配置文件")
            return False

    @staticmethod
    def _copy_file(src_path, dest_path):
        """
        将src_path复制到dest_path
        :return: 成功时返回True，失败时返回False
        """
        if os.path.exists(src_path) and os.path.isfile(src_path):
            try:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy(src_path, dest_path)
                print(f"COPY: {src_path} --> {dest_path}")
                return True
            except Exception as e:
                print(f"Exception: 无法将 {src_path} 复制到 {dest_path}. {e}")
                return False
        print(f"SKIP: {src_path} 不存在")
        return False


class Vim(ProfileBase):
    """Vim 的配置文件"""
    tool_name = "vim"
    host_filepath = os.path.join(ProfileBase.host_home_path, ".vimrc")
    rep_filename = ".vimrc"


# 支持的配置列表
PROFILE_DICT = {
    "vim": Vim(),
}
