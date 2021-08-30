from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'module designed to make your data preprocessing experience easier'
LONG_DESCRIPTION = 'these modules are all on my channel Islander Robotics where we belive in using python to ' \
                   'learn applications of Machine Learning and Artificial Intelligence through demonstration ' \
                   'this module is designed to make it easier on you during the data preprocessing stage for ' \
                   'your Machine Learning and Artificial Intelligence models'

# Setting up
setup(
    name="IslanderDataPreprocessing",
    version=VERSION,
    author="Islander Robotics (William McKeon",
    author_email="<IslanderRobotics@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["pandas","matplotlib","PyQt5","scikit-learn"],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)