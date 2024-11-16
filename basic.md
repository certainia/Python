### <div style="text-align: center; color: green;"> VS Code -->Git --> GitHub </div>

#### **1. 安装 Git**

1. **下载 Git**  
   前往 [Git 官方网站](https://git-scm.com/) 下载并安装 Git。

2. **验证安装**  
   安装完成后，在终端输入以下命令以确认安装成功：
   ```bash
   git --version
   ```

#### **2. 配置 Git**

1. **设置用户名和邮箱**  
   Git 使用这些信息标识提交者身份：
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```

2. **检查配置**

    使用以下命令检查已配置的用户名和邮箱：
    ```bash
    git config --list
    ```

#### **3.生成 SSH 密钥**

1. **生成SSH密钥对**
    在终端运行以下命令生成 SSH 密钥对：
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

2. **复制公钥**
    运行以下命令后复制公钥内容：
    ```bash
    cat ~/.ssh/id_rsa.pub
    ```
    将输出的内容复制到剪贴板。

3. **添加公钥到 GitHub**
    1. 登录 GitHub，进入 **Settings -> SSH and GPG keys -> New SSH key**。
    2. 粘贴公钥并保存。

4. **测试连接**
    使用以下命令测试 SSH 连接：
    ```bash
    ssh -T git@github.com
    ```

#### **4. 安装 VS Code 的 Git 插件** 
1. 打开 VS Code，进入扩展市场，搜索 GitLens 或 GitHub Pull Requests and Issues，并安装它们。
2. 配置插件：点击 VS Code 左下角齿轮图标，选择 Settings，搜索 Git，进行相关配置。

#### **5.克隆或连接 GitHub 仓库** 

1. **克隆仓库**

    1. 在 GitHub 仓库页面，点击 **Code -> SSH -> 复制仓库地址**。
    2. 在 VS Code 的终端运行以下命令克隆项目：
    ```bash
    git clone git@github.com:your_username/repository_name.git
    ```

2. **直接连接 GitHub 仓库**
    1. 在 VS Code 中按下 Ctrl+Shift+P（Mac: Cmd+Shift+P），搜索 Git: Clone。
    2. 粘贴仓库地址并选择存储路径

#### **6.推送代码到 GitHub** 
1. 添加文件到暂存区
    ```bash
    git add .
    ```

2. 提交更改
    ```bash
    git commit -m "Your commit message"
    ```

3. 推送到远程仓库
    ```bash
    git push origin main
    ```

---

#### **7.使用 VS Code 的内置 Git 功能** 
1. 在 VS Code 左侧工具栏点击 <b>Source Control</b> 图标
2. 进行文件更改、提交、推送操作，所有功能都可以通过图形界面完成。

### <div style="text-align: center; color: green;">Git提交代码指引</div>
#### 1. `git add`：将文件添加到暂存区

- **作用**：将你修改的文件从工作区（Working Directory）添加到 Git 的暂存区（Staging Area）。

- **使用方式**：
  - 添加单个文件：
    ```bash
    git add filename
    ```

  - 添加多个文件：
    ```bash
    git add file1 file2
    ```

  - 添加当前目录下的所有更改（包括新增、修改和删除）：
    ```bash
    git add .
    ```

  - 添加指定类型的文件：
    ```bash
    git add *.py
    ```

- **注意事项**：
  1. 添加文件到暂存区后，这些文件才会被记录在下一次提交中。
  2. 慎用 `git add .`，可能会意外添加不想提交的文件。

---

#### 2. `git commit -m`

- **作用**  
  `git commit -m` 用于将暂存区的更改提交到本地仓库，并附带一条提交说明。

- **语法**
  ```bash
  git commit -m "提交说明"
  ```
  
---

#### 3. `git push origin main`

- **作用**  
  `git push origin main` 用于将本地仓库的更改推送到远程仓库（如 GitHub、GitLab 等）的 `main` 分支。

- **语法**
  ```bash
  git push origin main
  ```

---

#### 4. 删除文件
1. 在目标仓库里
    删除文件或整个目录
    ```bash
    git rm 文件名
    git rm -r 目录名
    ```
2. 提交更改
    即将删除操作提交到本地 Git 仓库
    ```bash
    git commit -m "删除了不需要的文件/目录"
    ```
3. 推送到远程仓库
    即把更改同步到 GitHub
    ```bash
    git push
    ```

---

### <div style="text-align: center; color: green;">基本的终端命令</div>
#### 1. `cd` 指令：切换工作目录

- **作用**
`cd`（Change Directory）用于**切换工作目录**，将终端的当前工作目录更改为指定的路径。

- **语法**
  ```bash
  cd [目标路径]
  ```

- **用法**
    1. **切换到某个目录**  
        - **切换到当前目录的下一级文件夹**：
        ```bash
        cd MyCode
        ```
        - **直接切换到多级路径中的某个目录**：
        ```bash
        cd Projects/MyCode
        ```
        - **切换到绝对路径**：
        ```bash
        cd D:/Projects/MyCode
        ```
        在这些操作中，终端的当前工作目录将切换到指定的路径。

    2. **回到上一级目录**  
        使用 `..` 表示上一级目录：
        ```bash
        cd ..
        ```
        如果需要回到两级上层目录：
        ```bash
        cd ../..
        ```

    3. **回到根目录**  
        切换到当前盘符的根目录（Windows 环境）：
        ```bash
        cd /
        ```

    4. **切换到用户主目录**  
        使用 `~` 表示用户的主目录：
        ```bash
        cd ~
        ```
        用户主目录示例路径：
        - Windows: `C:\Users\yourname`
        - Unix/Linux: `/home/yourname`

    5. **切换到其他盘符（Windows 专用）**  
        直接输入盘符名即可切换到该盘符：
        ```bash
        D:
        ```
        **注意**：切换盘符后，默认不会进入某个目录。

- **注意事项**：
    1. `cd` 命令不会打开图形化窗口，只是改变终端的当前工作目录。
    2. 如果输入的路径不存在，会提示错误：
    ```bash
    The system cannot find the path specified.
    ```

    3. 为方便操作，可在路径中使用以下路径格式：
        - **相对路径**：相对于当前工作目录（如 `cd ../MyFolder`）。
        - **绝对路径**：指定完整路径（如 `cd D:/Projects/MyCode`）。

---

#### 2. `start` 指令：打开文件或程序

- **作用**
  `start` 用于**打开指定文件或目录**，它会在系统的默认图形化窗口中打开文件夹或程序。

- **语法**
  ```bash
  start [目标路径或文件名]
  ```

- **用法示例**
  
    1. **打开某个文件夹**
        ```bash
        start D:/Projects/MyCode
        ```
        在文件资源管理器中打开 `D:/Projects/MyCode` 文件夹。
    
    2. **打开某个文件**
        ```bash
        start README.md
        ```
        使用系统默认程序（如 VS Code 或记事本）打开 `README.md` 文件。
    
    3. **打开默认浏览器**
        ```bash
        在默认浏览器中打开 Google 的主页
        start https://google.com
        ```
        **使用 start + 网址 会通过系统默认的浏览器打开指定的网址
        如果网址包含特殊字符或空格，也可以将网址用引号括起来
        其实start对指定内容的访问同cd，包括cp mv re也服从系统的文件内容查找方式**
    
    4. **打开程序**
        ```bash
        start notepad
        ```
        打开记事本程序。
    
    5. **新建终端窗口**
        ```bash
        start cmd
        ```
        打开一个新的命令行窗口。

- **注意事项**
  
    1. 如果路径或文件名中有空格，需要用引号括起来：
        ```bash
        start "D:/My Folder/README.md"
        ```
    
    2. 不指定参数时，`start` 会打开一个新的命令行窗口。
        ```
        ```

---

#### 3. `dir`指令:列出当前文件夹下内容

- **适用环境**：Windows 系统（cmd 和 PowerShell）。
- **功能**：列出当前目录或指定目录中的所有文件和文件夹。

- **用法**：
    ```cmd
    dir [路径(默认就在目录不写)] [选项(需要再查，默认即可)]
    ```

---

#### 4. `ls`指令：同dir的非windows系列下的平替

- **适用环境**：Linux/Unix 系统（包括 macOS）。也可以在 Windows 中使用，但需要安装工具（如 Git Bash、Cygwin 或 Windows Subsystem for Linux）。
- **功能**：列出当前目录或指定目录中的文件和文件夹。

- **用法**：
    ```bash
    ls [路径(默认就在目录不写)] [选项(需要再查，默认即可)]
    ```

---

#### 5. `move(windows) or mv(非windows))`指令：文件和目录的移动

- **用法**：
    ```cmd
    move [源文件或目录] [目标文件或目录]
    ```
    ```bash
    mv   [源文件或目录] [目标文件或目录]
    ```
---

#### 6. `del(windows) or rm(非windows)` 指令：文件和目录的删除

- **用法**：
    ```cmd
    del [选项] 文件路径
    ```
    ```cmd
    rmdir [文件夹名] (文件夹为空)
    ```
    ```cmd
    rmdir /s [文件夹名] (文件夹非空)
    ```
    ```bash
    rm  [选项] [文件]
    ```
    ```bash
    re /r [选项] [目录]
    ```

- **说明**：
  - 在 Windows 中，`del` 用于删除文件，不能直接删除非空目录。
  - 在 Linux/Unix 系统中，`rm` 可用于删除文件和目录，配合 `-r` 选项可递归删除。

---

#### 7. `copy(windows) or cp(非windows)` 指令：文件和目录的复制

- **用法**：
    ```cmd
    copy [源文件路径] [目标路径]
    ```
    ```bash
    cp   [源文件路径] [目标路径] [选项(可放最后也可放cp后)]
    ```

- **说明**：
  - 在 Windows 中，`copy` 用于复制文件，复制目录需使用 `xcopy`。
  - 在 Linux/Unix 系统中，`cp` 用于复制文件和目录，配合 `-r`(即-Recurse) 选项可递归复制目录。

---

#### 8. 创建文件和文件夹
1. ##### 创建文件夹:使用 `mkdir` 命令创建文件夹。
-  语法
    ```bash
    mkdir 文件夹名称
    ```
2. ##### 创建文件:使用 `touch` 命令创建文件夹.
-  语法
    ```bash
    touch 文件名称
    ```
3. ##### 内容的写入
-  ##### 语法
    ```bash
    echo "Hello, World!" > example.txt
    ```
    - 如果文件已存在，这会覆盖内容。
    - 如果想追加内容而不覆盖，用 >>：
        ```
        echo "This is additional content." >> example.txt
        ```

---
<div style="text-align: center; color: blue;">未系统学习markdown，且水平不足，会在以后的使用中不断修改和增添新的内容</div>