import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "text-summarization"
AUTHOR_USER_NAME = "Josna-P"
SRC_REPO= "textSummarizer"
AUTHOR_EMAIL= "joshna.pitta@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="python package for NLP app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
)