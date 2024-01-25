#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from profile import PROFILE_DICT


def parse_opt():
    # all_keys 存储了目前程序支持的所有配置文件，其中 "all" 表示安装目前支持的所有配置文件
    all_keys = ["all"] + list(PROFILE_DICT.keys())

    parser = argparse.ArgumentParser()

    # --install 与 --restore 选项是互斥的，且至少要存在一个
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--install", type=str, nargs="+",
                       help=f"安装指定的配置文件，目前支持{all_keys}")
    group.add_argument("-r", "--restore", type=str, nargs="+",
                       help=f"恢复指定的配置文件，目前支持{all_keys}")
    opt = parser.parse_args()

    # 参数合法性检查
    input_list = opt.install if opt.install else opt.restore
    for key in input_list:
        if key not in all_keys:
            print(f"不支持 '{key}' 配置文件，请从 {all_keys} 中选择一个或多个配置")
            print(f"执行 python main.py -h 查看帮助文档")
            exit(-1)

    return opt


if __name__ == '__main__':
    opt = parse_opt()

    operation_type = "install"
    file_list = opt.install
    if opt.restore:
        operation_type = "restore"
        file_list = opt.restore

    print(f"operation type: {operation_type}")
    for key, value in PROFILE_DICT.items():
        if "all" in file_list or key in file_list:
            print(f"{operation_type} {key} profile...")
            getattr(value, operation_type)()  # 执行安装或恢复指令
    print("Done")
