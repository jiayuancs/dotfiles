" -----------------------------------------------------------------------------
" 基础配置
" -----------------------------------------------------------------------------

syntax on           " 语法高亮
set nocompatible    " 关闭 vi 兼容模式
set showmode        " 在底部显示当前是命令模式还是插入模式
set showcmd         " 命令模式下，在底部显示当前键入的命令
set mouse=a         " 允许使用鼠标点击定位(可使用shift+alt+鼠标选择指定区域，ctrl+c复制)
set encoding=utf-8  " UTF-8编码
set t_Co=256        " 启用256色
set background=dark " 使用黑色背景主题

" -----------------------------------------------------------------------------
" 代码缩进
" -----------------------------------------------------------------------------

filetype on         " 开启文件类型检测

" 载入与该类型对应的缩进规则（需要在 ~/.vim/indent/ 目录下编写对应语言的缩进规则）
filetype indent on

set autoindent      " 回车后自动缩进
set tabstop=4       " Tab显示的长度为4个空格(该命令不会将tab展开为空格)
set expandtab       " 将Tab展开为空格
set softtabstop=4   " Tab转为多少个空格

" 命令模式下输入">>","<<","=="分别执行增加一级缩进，取消一级缩进和取消全部缩进
set shiftwidth=4    " 自动缩进 4 个空格
" 关闭缩进不取整到 shiftwidth 的倍数
set noshiftround

" 针对 makefile 文件，取消展开Tab字符
autocmd FileType make set noexpandtab shiftwidth=4 softtabstop=0

" -----------------------------------------------------------------------------
" 外观
" -----------------------------------------------------------------------------

" 行号相关配置
set number           " 显示行号
set relativenumber   " 相对行号
set cursorline       " 在光标所在的当前行显示下划线

" 折行相关配置
set textwidth=80     " 行宽，即一行显示多少个字符
set nowrap           " 关闭自动折行(自动折行: 太长的行分成几行显示)
" set linebreak        " 不在单词内部折行
" set wrapmargin=2     " 折行处与编辑窗口的右边缘之间空出的字符数

" 光标滚动相关配置
set scrolloff=6      " 垂直滚动时，光标距离顶部/底部的距离(单位: 行)
set sidescrolloff=12 " 水平滚动，光标距离行首或行尾的位置(单位：字符)

" 底部状态栏相关配置
" 是否显示状态栏(底部显示文件名称)。0 表示不显示，1 表示只在多窗口时显示，2 表示显示。
set laststatus=2
" 是否显示标签栏(顶部显示文件名成)。0 表示不显示，1 表示创建标签页后才显示标签栏，2 表示总是显示。
set showtabline=2
set ruler            " 在状态栏显示光标的当前位置(位于哪一行哪一列)

" -----------------------------------------------------------------------------
" 搜索
" -----------------------------------------------------------------------------

" 光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set showmatch

" 搜索时高亮
set hlsearch

" 输入每个字符都会进行搜索（增量搜索）
set incsearch

" 高亮显示匹配的括号
set showmatch

" 搜索时不区分大小写
set ignorecase
" 如果搜索时输入的字符全是小写，则按照不区分大小写进行搜索;
" 如果搜索时输入的字符包含大写字符，则按区分大小写进行搜索.
set smartcase

" -----------------------------------------------------------------------------
" 编辑
" -----------------------------------------------------------------------------

" 将工作目录自动切换到正在编辑的文件的目录(主要用在一个 Vim 会话之中打开多个文件的情况)
set autochdir

set noerrorbells        " 出错时不要发出响声
set novisualbell        " 出错时不发出视觉提示(视觉提示: 通常是屏幕闪烁)

" 需要记住多少次历史操作
" set history=1000

" 打开文件监视。如果在编辑过程中文件发生外部改变(比如被别的编辑器编辑了)，就会发出提示
set autoread

" 启用命令补全
set wildmenu
" 命令模式下，底部操作指令按下 Tab 键自动补全。
" 第一次按下 Tab，会显示所有匹配的操作指令的清单；
" 第二次按下 Tab，会依次选择各个指令。
set wildmode=longest:list,full

" 即使开启了行号，拷贝时也不会把行号拷过去
set copyindent
