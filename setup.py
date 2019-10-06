import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pywalblur',
    version='1.0',
    description='blr background on window opening',
    author='Moussa Fofana',
    author_email='moussa.fofana@epitech.eu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Di-KaZ/pywalblur",
    packages=setuptools.find_packages(),
    install_requires=['ewmh'],
    python_requires='>=3.6',
)