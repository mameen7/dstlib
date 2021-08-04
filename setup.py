from setuptools import setup

setup(
    name='dstlib',
    version='1.2',
    description='Data structures python library',
    url="https://github.com/algebra7/dstlib",
    packages=['dstlib'],
    author='Ahmad M Ameen',
    author_email='ahmadmameen7@gmail.com',
    long_description=open("README.rst").read(),
    package_dir={"data_structures": "dstlib"},
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
