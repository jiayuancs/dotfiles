# dotfiles

自动导入 Linux 中常用工具的配置文件。

## 支持的工具

- [x] vim
- [ ] bash
- [ ] ssh
- [ ] git

## 使用方法

clone 仓库

```shell
git clone git@github.com:jiayuancs/dotfiles.git
cd dotfiles
```

安装配置文件：

```shell
# 安装所有配置
python main.py --install all

# 仅安装 vim 的配置
python main.py --install vim

# 同时安装 vim 和 ssh 的配置
python main.py --install vim ssh
```

恢复配置：

```shell
# 恢复所有配置
python main.py --restore all

# 仅恢复 vim 的配置
python main.py --restore vim

# 同时恢复 vim 和 ssh 的配置
python main.py --restore vim ssh
```

## 添加额外配置文件支持

为该仓库脚本添加额外的配置文件支持只需如下三个步骤：

1. 在 [profile](./profile) 目录下创建相应的配置文件
2. 在 [profile.py](./profile.py) 中实现该配置文件对应的类
3. 将该类添加到 [profile.py](./profile.py) 文件中的 `PROFILE_DICT` 字典中

示例如下（添加 bash 配置文件支持）：

1. 在 [profile](./profile) 目录下创建并编写 `.bashrc` 文件（文件名可自定义）：

    ```shell
    vim ./profile/.bashrc
    ```
2. 在 [profile.py](./profile.py) 中实现该配置文件对应的类，这里将类名定义为 `Bash`，以表示其是 bash 的配置文件：

    ```Python
    # 类中只需要定义如下三个类属性即可
    class Bash(ProfileBase):
        """Bash 的配置文件"""
        # tool_name 是工具的名称(可自定义)
        tool_name = "bash"
   
        # host_filepath 是该工具(这里为Bash)的配置文件在主机中的绝对路径;
        # ProfileBase.host_home_path 是当前用户的家目录。
        host_filepath = os.path.join(ProfileBase.host_home_path, ".bashrc")
   
        # 仓库中配置文件的文件名，这里必须与步骤1中创建的文件名一致
        rep_filename = ".bashrc"
    ```

3. 将定义好的 `Bash` 类添加到 [profile.py](./profile.py) 文件中的 `PROFILE_DICT` 字典中：

    ```Python
    # 支持的配置列表
    PROFILE_DICT = {
        "vim": Vim(),
        "bash": Bash(), # 添加到这里
    }
    ```

至此，脚本便支持安装恢复 bash 的配置文件
