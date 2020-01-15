""" lambdata -a collection of data science helper functions
"""

import setuptools

REQUIRED = [
	"numpy",
	"pandas"
]

with open("README.md", "r") as fh:
	LONG_DESCRIPTION = fh.read()

setuptools.setup(
        name = "lambdata_qj",
        version = "0.0.3",
        author = "qianjing",
        description="A collection of data science helper functions",
        long_description= LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/qianjing2020/unit3_project/",
        packages=setuptools.find_packages(),
        python_requires=">=3.5",
        install_requires= REQUIRED,
        classifiers=[
		"Programming Language :: Python :: 3",
        	"License :: OSI Approved :: MIT License",
        	"Operating System :: OS Independent",
        	],
        )	 
