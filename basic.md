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

1. **生成 SSH 密钥对**
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

### <div style="text-align: center; color: green;">Git 提交代码指引</div>

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

     1. 使用 start + 网址 会通过系统默认的浏览器打开指定的网址
     2. 如果网址包含特殊字符或空格，也可以将网址用引号括起来
     3. 其实 start 对指定内容的访问同 cd，包括 cp mv re 也服从系统的文件内容查找方式

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

#### 4. `ls`指令：同 dir 的非 windows 系列下的平替

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
  rmdir -s [文件夹名] (文件夹非空)
  ```

  ```bash
  rm  [选项] [文件]
  ```

  ```bash
  rm -r [选项] [目录]
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

  ```cmd
  xcopy [源目录路径] [目标路径]
  ```

  ```bash
  cp [源文件路径] [目标路径]
  ```

  ```bash
  cp -r [源目录路径] [目标路径] (或者后置-Recurse)
  ```

- **说明**：
  - 在 Windows 中，`copy` 用于复制文件，复制目录需使用 `xcopy`。
  - 在 Linux/Unix 系统中，`cp` 用于复制文件和目录，配合 `-r`(即-Recurse) 选项可递归复制目录。

---

#### 8. 创建文件和文件夹

1. ##### 创建文件夹:使用 `mkdir` 命令创建文件夹。

- 语法
  ```bash
  mkdir 文件夹名称
  ```

2. ##### 创建文件:使用 `touch` 命令创建文件.

- 语法
  ```bash
  touch 文件名称
  ```

3. ##### 内容的写入

- ##### 语法
  ```bash
  echo "Hello, World!" > example.txt
  ```
  - 如果文件已存在，这会覆盖内容。
  - 如果想追加内容而不覆盖，用 >>：
    ```
    echo "This is additional content." >> example.txt
    ```

---

#### 8. Shell（命令行/文件匹配）中通配符

##### `*`（匹配任意多个字符，包括空字符）

- **用法**  
   匹配文件名和路径。
- **示例**：
  - `ls *.txt`：匹配当前目录下所有以 `.txt` 结尾的文件。
  - `ls *`：匹配当前目录下所有文件和文件夹。

##### `?`（匹配单个任意字符）

- **用法**
  匹配一个字符(匹配几个写几个即可)
- **示例**：
  - `ls file?.txt`：匹配 `file1.txt`、`file2.txt`，但不匹配 `file10.txt`。
- **说明**：
  - 如果需要匹配两个或多个字符，可以通过 _ 和 ? 结合使用(可类推更多以上)：
    `ls file??_.txt`
  - Shell 本身的通配符（\*, ?）对匹配长度的控制有限，比如匹配长度为 2 到 5 个字符：
    `ls file?? file??? file???? file?????`

##### `[]`（匹配指定范围的单个字符）

- **用法**
  用于匹配一个范围内的字符。
- **示例**：
  - `ls file[1-3].txt`：匹配 `file1.txt`、`file2.txt`、`file3.txt`。
  - `ls file[abc].txt`：匹配 `filea.txt`、`fileb.txt`、`filec.txt`。

##### `~`（表示用户的主目录）

- **用法**
  `~` 代表当前用户的主目录。
- **示例**：
  - `cd ~`：切换到当前用户主目录。
  - `ls ~/Documents`：列出主目录下的 `Documents` 文件夹内容。

##### `{}`（生成匹配的组合）

- **用法**
  用于列举匹配的选项。
- **示例**：
  - `cp file{1,2}.txt /backup/`：复制 `file1.txt` 和 `file2.txt` 到 `/backup/` 目录。
  - `echo {a,b,c}.txt`：输出 `a.txt b.txt c.txt`。

#### 9.`{}` 通配符详解

##### 1.基本用法

- **语法**
  ```bash
  {option1,option2,...}
  ```
- {} 中列举的选项将被逐一替换到命令中运行。
- 每个选项之间用逗号分隔。

- **示例**

  ```bash
  echo file{1,2,3}.txt
  ```

- **输出**
  ```bash
  file1.txt file2.txt file3.txt
  ```

##### 2.与路径结合使用

- **与路径结合使用，生成不同的文件或目录路径。**
- **语法**

  ```bash
  mkdir project/{src,bin,docs}
  ```

- **创建了以下目录结构:**
  ```bash
  project/src
  project/bin
  project/docs
  ```

##### 3.组合多个层级

- **可以在 {} 中嵌套路径组合，生成更复杂的结构**
- **示例**
  ```bash
  echo /usr/{local,bin}/{lib,share}
  ```
- **输出**
  ```bash
  /usr/local/lib /usr/local/share /usr/bin/lib /usr/bin/share
  ```
  每个选项的组合都会被生成

##### 4.范围拓展

- **数字范围**
  ```bash
  echo file{1..5}.txt
  ```
- **输出**

  ```bash
  file1.txt file2.txt file3.txt file4.txt file5.txt
  ```

- **字母范围**
  ```bash
  echo {a..c}
  ```
- **输出**
  ```bash
  a b c
  ```

##### 5.添加前缀和后缀

- **示例**
  ```bash
  echo test-{a,b,c}-file
  ```
- **输出**
  ```bash
  test-a-file test-b-file test-c-file
  ```

##### 5.添加前缀和后缀

- **批量操作文件**
  ```bash
  cp file{1,2,3}.txt /backup/
  ```
- **将 file1.txt、file2.txt、file3.txt 复制到 /backup/ 目录。**
- **清理文件**
  ```bash
  rm report-{draft,final}.pdf
  ```
- **删除 report-draft.pdf 和 report-final.pdf 文件。**
- **构建测试目录**
  ```bash
  mkdir test-{1..5}/{input,output}
  ```
- **结果: 创建以下目录结构：**
  ```bash
  test-1/input
  test-1/output
  test-2/input
  test-2/output
  ...
  test-5/input
  test-5/output
  ```

###### 注意事项

1. **不支持嵌套 `{}`**

   - `{}` 本身不支持递归嵌套，例如 `{a,{b,c}}` 是不允许的。

2. **与通配符不同**

   - `{}` 是明确列举的组合，而通配符如 `*` 是匹配文件系统中的实际文件。

3. **Shell 限制**
   - `{}` 的功能依赖于 Shell，只有支持这种扩展的 Shell（如 Bash、Zsh）才可以使用。

#### 9.echo 的使用

- **`echo` 是一个非常基础的命令，在 **Shell** 或 **命令行环境\*\* 中，主要用于打印文本或输出内容到终端。它经常用于显示字符串、变量值，或者与其他命令结合生成复杂的输出。

**语法**

```bash
echo [选项] [字符串]
```

**功能**

- 将字符串显示在终端上。
- 可以结合通配符或范围扩展 `{}` 输出动态内容。

**1. 打印普通文本**

```bash
echo "Hello, World!"
```

**输出：**

```
Hello, World!
```

2. 结合 `{}` 打印多个组合** `{}` 可用于生成范围或组合，`echo` 会把它们展开后显示。**示例：路径组合\*\*

```bash
echo /usr/{local,bin}/{lib,share}
```

**输出：**

```bash
/usr/local/lib /usr/local/share /usr/bin/lib /usr/bin/share
```

**示例：生成文件名**

```bash
echo file{1..5}.txt
```

**输出：**

```
file1.txt file2.txt file3.txt file4.txt file5.txt
```

**示例：生成字母序列**

```bash
echo {a..c}
```

**输出：**

```css
a b c
```

**3. 打印变量值** `echo` 可以用来显示 Shell 中的变量内容。**示例**

```bash
name="Alice"
echo "Hello, $name!"
```

**输出：**

```
Hello, Alice!
```

**4. 打印换行符或特殊字符** 默认情况下，`echo` 会将字符串按行输出。如果需要特殊字符（如换行符）或避免换行，可以结合选项使用：**-n** （取消换行）

```bash
echo -n "No newline at the end"
```

**输出：**

```arduino
No newline at the end
```

**-e** （支持转义字符）

```bash
echo -e "Line1\nLine2"
```

**输出：**

```
Line1
Line2
```

**5. 重定向输出** `echo` 的输出可以通过重定向符号 `>` 保存到文件中。**示例：保存到文件**

```bash
echo "Hello, File!" > example.txt
```

- **效果：** 文件 `example.txt` 中会保存：

```arduino
Hello, File!
```

**6. 配合通配符使用** `echo` 也可以结合通配符（如 `*` 和 `?`），用于动态生成文件名或路径。**示例**

```bash
echo file?.txt
```

**假设目录中有：**

```
file1.txt file2.txt file3.txt
```

**输出：**

```
file1.txt file2.txt file3.txt
```

---

**总结**

- `echo` 的主要用途是 **打印内容到终端** 。
- 结合 `{}`、通配符、变量或重定向，可以用于生成动态内容或保存到文件。

<div style="text-align: center; color: blue;">本人水平受限，会在以后的使用中不断修改和增添新的内容</div>
