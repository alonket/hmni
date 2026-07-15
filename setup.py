from pathlib import Path

from setuptools import find_packages, setup


# torch is omitted from install_requires so pip does not resolve it from PyPI's
# default CUDA wheels when hmni is installed as a git dependency (e.g. in Docker).
# Install CPU torch explicitly before hmni; see README.md.
_INSTALL_EXCLUDES = {"torch"}


def load_requirements(path: str = "requirements.txt") -> list[str]:
  """Load install_requires from requirements.txt (single source of truth)."""
  requirements = []
  for line in Path(path).read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#") or line.startswith("--"):
      continue
    if line.startswith("git+"):
      line = f"abydos @ {line}"
    name = line.split("@", 1)[0].split("[", 1)[0].strip()
    name = name.partition(">")[0].partition("<")[0].partition("=")[0].partition("!")[0].strip()
    if name in _INSTALL_EXCLUDES:
      continue
    requirements.append(line)
  return requirements


setup(
    name="hmni",
    version="0.1.9",
    author="Christopher Thornton",
    author_email="christopher_thornton@outlook.com",
    description="Fuzzy Name Matching with Machine Learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Christopher-Thornton/hmni",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements(),
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
) 