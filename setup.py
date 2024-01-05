import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as f:
    requirements = f.read()


setuptools.setup(
  name = 'dorothy',
  version = '1.0.2',
  license='GPL-3.0',
  description = '',
  long_description = long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  author = 'João Victor da Fonseca Pinto',
  author_email = 'jodafons@lps.ufrj.br,jodafons@cern.ch',
  url = 'https://github.com/bric-tb-softwares/dorothy',
  keywords = ['framework', 'threading', 'shared resources', 'flexibility', 'python', 'online'],
  install_requires=requirements,
  classifiers=[],
)
