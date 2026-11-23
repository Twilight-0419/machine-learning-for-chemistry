上机作业 2：Logistic 回归与基因表达数据分类（学生版）

一、下载与解压：本次提供两个附件
1. hw2-student.zip：作业模板、课堂示例、环境配置、本说明和小型性别标签文件。
2. hw2-data.zip：大型基因表达原始数据 GTEx_gene_amygdala_tpm_v8.gct。

两个 ZIP 都带有顶层 hw2 文件夹。请将它们解压到同一个可写的父目录，合并同名的 hw2 文件夹。
例如：都解压到 D:/mlcourse，最终应得到 D:/mlcourse/hw2。
不要直接在压缩包内运行，也不要把数据 ZIP 再解压到现有 hw2 目录内部，以免形成 hw2/hw2。

合并后必须具有以下结构（gene.ipynb 与 mlchem-2024fall_v1 文件夹并列）：
hw2/
  gene.ipynb
  lab2-logistic-regression-assessment.ipynb
  environment_minimal.yml
  README.txt
  mlchem-2024fall_v1/
    GTEx_gene_amygdala_tpm_v8.gct
    subject_pheontypes_v8.txt

二、配置环境并运行
1. 打开 Miniforge Prompt（Windows）或终端（macOS / Linux），进入解压后的 hw2 目录。
   例如，在 Windows 的 Miniforge Prompt 中输入：
   cd /d D:\mlcourse\hw2
   macOS / Linux 示例：
   cd ~/mlcourse/hw2
   请将示例路径替换为自己的实际路径。
2. 首次创建课程环境（推荐 Python 3.12）：
   conda env create -f environment_minimal.yml
   如果已经有 mlchem 环境，则使用下面这条更新命令：
   conda env update -n mlchem -f environment_minimal.yml
3. 激活环境并启动 JupyterLab：
   conda activate mlchem
   jupyter lab
4. 在 JupyterLab 中打开 gene.ipynb，选择 mlchem 环境的 Python 内核，按顺序阅读并完成各任务。
   请从 hw2 目录启动，以便相对路径能够找到数据。
   lab2-logistic-regression-assessment.ipynb 是课堂示例，供学习和参考，本身无需答题。

三、作答要求
在 BEGIN YOUR SOLUTION / END YOUR SOLUTION 标记之间填写代码或文字回答。
任务 1.1、1.2、3.1、3.2 的函数尚未实现，初次调用出现 NotImplementedError 是预期提示。
请保留原测试单元格，不修改测试内容；文字答题区逐行使用 # 注释。
完成后重启内核，从头运行全部单元格，检查结果并保存 gene.ipynb。

四、提交方法：提交大型 .gct 原始数据以外的作业文件
1. 将完成作业的 hw2 文件夹复制一份，命名为“学号-姓名-第二次上机作业”，用作提交副本。
2. 在提交副本中排除这个大型文件：
   mlchem-2024fall_v1/GTEx_gene_amygdala_tpm_v8.gct
   保留小型标签文件 mlchem-2024fall_v1/subject_pheontypes_v8.txt。
   本地运行目录中的 .gct 数据文件请保留，便于之后继续运行。
3. 提交副本保留其余作业文件：已完成并保存输出的 gene.ipynb、课堂示例、
   environment_minimal.yml、README.txt、小型标签文件，以及自己新增的代码、图片和结果文件。
4. 如果使用自行配置的 conda 环境，建议先激活该环境并执行：
   conda env export > environment.yml
   将生成的 environment.yml 一起放入提交副本。
5. 将提交副本压缩为“学号-姓名-第二次上机作业.zip”，在教学网本作业入口提交。
   示例：200XXXXXXX-张三-第二次上机作业.zip。
   不要把下载的 hw2-data.zip、hw2-student.zip、虚拟环境或缓存目录再次装入提交包。

提交前检查：
- gene.ipynb 已完成 read_gct、normalize_tpms、evaluate_model、train_and_eval 四个函数。
- gene.ipynb 已填写任务 3.3、问题 4.1、4.2、4.3 的文字回答。
- 重启内核并从头运行后，原有测试通过，且已保存饼图、评估指标、ROC 曲线和基因分析输出。
- 提交 ZIP 保留除大型 .gct 数据外的作业文件、小型标签文件和自己新增的代码/结果。
- 提交 ZIP 中没有大型 .gct 数据、原始数据 ZIP、虚拟环境、__pycache__ 或 .ipynb_checkpoints。
- 压缩包名为本人学号-本人姓名-第二次上机作业.zip。

作业截止时间与具体提交入口以教学网最终发布的要求为准。

数据说明：提供的 GCT 文件实际包含 152 份样本、56200 个基因特征。
文件头仍标记 154 个样本，读取时应以实际样本列为准。
