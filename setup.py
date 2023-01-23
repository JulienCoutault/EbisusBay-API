from setuptools import setup

setup(
    name="ebisusbay",
    version='0.0.3',
    description='Python Wrapper for ebisusbay.com API',
    long_description_content_type='text/markdown',
    url='https://github.com/JulienCoutault/EbisusBay-API',
    author='Programmateur01',
    author_email='ebisusbay-api@juliencoutault.fr',
    project_urls={
        'Source': 'https://github.com/JulienCoutault/EbisusBay-API'
    },
    keywords=['Cronos', 'API', 'CRO', 'Blockchain', 'NFT', 'ebisusbay.com'],
    license='MIT',
    packages=['ebisusbay'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
