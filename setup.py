from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = "Just a random api"
LONG_DESCRIPTION = "Just a random api that I have created."


setup(
    name="scratchclickerwebsiteapi",
    version=VERSION,
    author="Aleksanser Sapieha",
    author_email="<aleksander.sapieha@scratch-clicker.digital>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'scratch', 'scratch clicker', 'scratch clicker api', 'clicker', 'game', 'gamejolt', 'itch', 'classic'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)