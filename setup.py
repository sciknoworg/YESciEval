from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="YESciEval",
    version="0.2.0",
    author="Hamed Babaei Giglou",
    author_email="hamedbabaeigiglou@gmail.com",
    description="YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sciknoworg/YESciEval",
    packages=find_packages(),
    install_requires=[
        "pre-commit",
        "transformers,"
        "torch",
        "peft",
        "openai",
        "pandas",
        "numpy",
        "pydantic",
        "pytest"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<4.0.0",
    project_urls={
        "Documentation": "https://yescieval.readthedocs.io/",
        "Source": "https://github.com/sciknoworg/YESciEval",
        "Tracker": "https://github.com/sciknoworg/YESciEval/issues",
    },
)
