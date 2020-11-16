import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="smart-status-bar",
    version="1.0.3",
    author="Shreyansh Nagpal",
    author_email="shreyanshnagpal7499@gmail.com",
    description="A smart status bar for loops.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shreyansh7499/smart-status-bar",
    packages=['smart_status_bar'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
