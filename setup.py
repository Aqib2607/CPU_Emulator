from setuptools import setup, find_packages

setup(
    name='VirtualCPUEmulator',
    version='0.1.0',
    packages=find_packages(), 
    install_requires=[
        'pytest>=6.0',
        'numpy>=1.21',
        'matplotlib>=3.4',
    ],
    author='Aqib Jawwad Nahin',
    author_email='aqibjawwad2607@google.com',
    description='A Python-based Virtual CPU Emulator for educational purposes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Aqib2607/Virtual_CPU_Emulator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
