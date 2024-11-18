import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Get the current directory path where setup.py is located
here = os.path.abspath(os.path.dirname(__file__))

# Define the Cython extension
extensions = [
    Extension(
        # Module name with full package path
        # This will ensure that the compiled .so file is correctly referenced in the Python package
        "mz_tree",

        # Path to the Cython .pyx source file
        [os.path.join(here, "mz_tree.pyx")],

        # Include directories to find necessary header files
        include_dirs=[
            np.get_include(),  # Include NumPy headers
            os.path.join(here, "../common_lib")  # Include headers from the common_lib directory
        ],

        # Compiler arguments to use C++11 standard
        extra_compile_args=["-std=c++11"],
        # Linker arguments to use C++11
        extra_link_args=["-std=c++11"],

        # Specify that the extension is in C++
        language="c++",
    )
]

# Setup function to build the extension
setup(
    name="LightZero",  # Name of the package
    ext_modules=cythonize(
        extensions,  # Pass the extensions list
        build_dir=here,  # Build the .so file in the same directory as `setup.py`
        language_level=3  # Use Python 3 syntax in Cython
    ),
)