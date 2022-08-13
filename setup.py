from setuptools import setup

setup(
    name='garlandtools',
    version='1.0.0',
    description='Python PIP module for GarlandTools',
    url='https://github.com/Sakul6499/GarlandTools-PIP',
    author='Lukas Weber',
    author_email='me@sakul6499.de',
    license='MIT License',
    packages=['garlandtools'],
    long_description="Unofficial Python wrapper for [GarlandTools](https://garlandtools.org/) API. Check the [GitHub Repository](https://github.com/Sakul6499/GarlandTools-PIP) for more information.",
    long_description_content_type='text/markdown',
    install_requires=['mpi4py>=2.0',
                      'requests>=2.0'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
)
