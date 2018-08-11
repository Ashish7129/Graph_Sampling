import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Graph Sampling",
    version="0.0.1",
    author="Ashish Aggarwal",
    author_email="ashish.mcs16.du@gmail.com",
    description="Graph Sampling Package",
    long_description="A Graph Sampling package containing various approaches which samples the original graph according to different sample sizes",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
