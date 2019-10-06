import setuptools
import WallaBlur

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='WallaBlur',
    version='1.0.1',
    author='Moussa Fofana',
    author_email='moussa.fofana@epitech.eu',
    description='blur background on window opening',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Di-KaZ/WallaBlur",
    packages=["WallaBlur"],
    entry_points={"console_scripts": ["wab=WallaBlur.__main__:main"]},
    install_requires=['ewmh'],
    python_requires='>=3.6',
)