import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sampling",
    version="0.0.1",
    author="Ashish Aggarwal",
    author_email="ashish.mcs16.du@gmail.com",
    description="A Sampling Package",
    long_description="A Sampling package containing various techniques which samples the original graph according to the sizes",
    long_description_content_type="text/Sampling_t",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
