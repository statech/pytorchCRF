import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(ROOT_DIR, 'README.md')) as file:
    readme = file.read()

setup(
    name='pytorchcrf',
    version='0.1',
    description='PyTorch CRF with N-best decoding',
    long_description=readme,
    url='https://github.com/statech/pytorch-crf',
    author='Feiyang Niu',
    author_email='statech.forums@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='pytorch crf nbest',
    packages=find_packages(),
    python_requires='>=3.6',
)