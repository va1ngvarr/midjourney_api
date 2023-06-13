from setuptools import setup, find_packages


setup(
    name="midjourney_unofficial_api",
    version="1.0",
    license="MIT",
    author="Igor Vasilev",
    author_email="va1ngvarr@gmail.com",
    packages=find_packages("midjourney"),
    package_dir={"": "midjourney"},
    url="https://github.com/va1ngvarr/midjourney_api",
    keywords="midjourney neuronetwork ml ml_python",
    install_requires=["requests", "pandas"],
)
