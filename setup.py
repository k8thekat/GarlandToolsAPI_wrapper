from setuptools import setup

setup(
    name='garlandtools',
    version='0.1.0',    
    description='Python PIP module for GarlandTools',
    url='https://github.com/Sakul6499/GarlandTools-PIP',
    author='Lukas Weber',
    author_email='me@sakul6499.de',
    license='MIT License',
    packages=['garlandtools'],
    install_requires=['mpi4py>=2.0',
                      'requests>=2.0'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)