import setuptools

setuptools.setup(
    name="etsy_scrappers",
    version="0.1.0",
    author="Vadim Makarov",
    author_email="add4che@gmail.com",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/run4w4y/etsy_scrappers",
    packages=setuptools.find_packages(),
    install_requires=[
        'httpx',
        'async_web_scrapper @ http://github.com/run4w4y/async_web_scrapper/archive/main.tar.gz',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)