# -*- coding: utf-8 -*-
"""
一个使用标准 LaTeX (article 类) 生成 PDF 简历的 Python 脚本。
此版本无需安装额外的 'AltaCV' 等模板，兼容性更好。

如何运行:
1. 确保你的电脑上安装了 LaTeX 发行版 (如 TeX Live, MiKTeX)。
2. 确保 `xelatex` 命令可以在你的终端中运行。
3. 运行此脚本: python create_resume.py
4. 一个名为 'Hongnan_Lin_Resume_LaTeX.pdf' 的文件将会被创建。
"""
import subprocess
import os

# --- LaTeX 模板和内容 ---
# 使用标准的 article 类，兼容性极佳
latex_template = r"""
\documentclass[10pt,a4paper]{article}

% --- 基础包和页面设置 ---
\usepackage{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{hyperref} % 用于创建可点击的链接
\usepackage[T1]{fontenc}
\usepackage{titlesec} % 用于自定义节标题

% 设置页面边距
\geometry{a4paper, margin=0.8in}

% --- 字体设置 ---
% 设置英文字体 (Carlito/Calibri 是常见的无衬线字体)
\setmainfont{Carlito}
% 设置中文字体 (KaiTi 是 Windows 自带的标楷体, HeiTi (黑体) 也是不错的选择)
\setCJKmainfont{KaiTi}

% --- 自定义格式 ---
% 移除页码
\pagestyle{empty}

% 自定义节标题格式，使其更紧凑
\titlespacing*{\section}{0pt}{1.5ex}{1ex}
\titlespacing*{\subsection}{0pt}{1ex}{0.5ex}
\titleformat{\section}{\Large\scshape\raggedright}{\thesection}{1em}{}[\titlerule]

% --- 文档开始 ---
\begin{document}

% --- 页眉：姓名和联系信息 ---
\begin{center}
    {\Huge\bfseries 林泓楠 (Hongnan Lin)}
    \vspace{4pt}
    
    \rule{\textwidth}{0.4pt}
    \vspace{2pt}
    
    Email: \href{mailto:hongnanlin390@gmail.com}{hongnanlin390@gmail.com} \quad | \quad 
    GitHub: \href{https://github.com/LinLoveZyt}{github.com/LinLoveZyt} \quad | \quad 
    Edu Email: \href{mailto:202430580649@mail.scut.edu.cn}{202430580649@mail.scut.edu.cn}
    
    \rule{\textwidth}{0.4pt}
\end{center}

% --- 个人简介 ---
\section*{个人简介 (Summary)}
华南理工大学计算机科学拔尖班大一（准大二）学生。对通过代码将创意变为现实充满热情。具备三维重建 (NeRFs/3DGS)、视频理解 (DETR/LVLM) 的学习经历，并独立开发过多个多智能体系统项目，拥有扎实的编程基础和快速学习能力。

% --- 项目经历 ---
\section*{项目经历 (Projects)}
\subsection*{Auto\_Arxiv \hfill \textit{独立开发}}
\begin{itemize}
    \setlength\itemsep{0em} % 减少列表项间距
    \item 开发了一个多智能体科研助手，可自动追踪、总结和归类 arXiv 上的最新论文。
    \item 实现了基于个性化需求生成调研报告的功能，并构建本地知识库以支持科研问答。
    \item \textbf{技术栈:} Python, Multi-Agent, LangChain, Ollama
\end{itemize}

\subsection*{Study\_Chicken \hfill \textit{独立开发 (进行中)}}
\begin{itemize}
    \setlength\itemsep{0em}
    \item 设计并开发一个在线番茄钟，集成基于图像感知的深度学习算法，实时分析用户学习专注度。
    \item \textbf{技术栈:} Python, Deep Learning, ResNet50, Computer Vision
\end{itemize}

\subsection*{MathSolver \hfill \textit{独立开发 (竞赛项目)}}
\begin{itemize}
    \setlength\itemsep{0em}
    \item 构建了一个基于 Python 工具增强的多智能体系统，旨在协作解决复杂的数学问题。(注：项目细节因参与比赛暂不公开)
    \item \textbf{技术栈:} Python, Multi-Agent, Tool Enhancement
\end{itemize}

% --- 专业技能 ---
\section*{专业技能 (Skills)}
\begin{itemize}
    \setlength\itemsep{0em}
    \item \textbf{编程语言与框架:} Python (PyTorch, LangChain), C++, Kotlin
    \item \textbf{工具与平台:} Docker, Git, GitHub
    \item \textbf{专业领域:} 多智能体系统 (Multi-Agent Systems), 深度学习 (Deep Learning), 计算机视觉 (Computer Vision)
\end{itemize}

% --- 教育背景 ---
\section*{教育背景 (Education)}
\textbf{华南理工大学 (South China University of Technology)} \hfill \textbf{2024 - 至今} \\
计算机科学与工程学院 | 计算机科学拔尖基地班

\end{document}
"""

def create_latex_resume():
    """
    Generates a .tex file and compiles it into a PDF using xelatex.
    """
    tex_filename = "resume"
    pdf_filename = "Hongnan_Lin_Resume_LaTeX.pdf"
    
    # Write the .tex file using utf-8 encoding
    try:
        with open(f"{tex_filename}.tex", "w", encoding="utf-8") as f:
            f.write(latex_template)
        print(f"✅ 成功写入 '{tex_filename}.tex' 文件。")
    except IOError as e:
        print(f"❌ 写入 .tex 文件时出错: {e}")
        return

    # Compile twice to ensure all references and formats are correct
    print("🚀 开始使用 xelatex 编译 PDF...")
    for i in range(2):
        print(f"  -> 编译第 {i+1} 次...")
        try:
            process = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", f"{tex_filename}.tex"],
                capture_output=True, text=True, encoding="utf-8"
            )
            if process.returncode != 0:
                print(f"❌ 编译第 {i+1} 次失败。")
                print("--- LaTeX 错误日志 ---")
                # Only print the last few lines of the log for brevity
                log_lines = process.stdout.splitlines()
                for line in log_lines[-15:]:
                    print(line)
                print("----------------------")
                print("请检查你的 LaTeX 环境和 'resume.log' 文件以获取详细错误信息。")
                return
        except FileNotFoundError:
            print("❌ 命令 'xelatex' 未找到。")
            print("请确保你的 LaTeX 发行版 (TeX Live, MiKTeX) 已安装并已添加到系统的 PATH 环境变量中。")
            return
        except Exception as e:
            print(f"❌ 编译过程中发生未知错误: {e}")
            return
    
    print(f"✅ 编译成功！PDF 文件已生成: '{pdf_filename}'")
    
    # Clean up auxiliary files
    print("🧹 正在清理临时文件...")
    extensions_to_clean = ["aux", "log", "out", "tex"]
    try:
        if os.path.exists(f"{tex_filename}.pdf"):
            os.rename(f"{tex_filename}.pdf", pdf_filename) # Rename
        for ext in extensions_to_clean:
            if os.path.exists(f"{tex_filename}.{ext}"):
                os.remove(f"{tex_filename}.{ext}")
        print("✨ 清理完成！")
    except Exception as e:
        print(f"⚠️ 清理文件时出错 (可忽略): {e}")


if __name__ == "__main__":
    create_latex_resume()