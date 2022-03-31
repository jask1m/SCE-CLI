import setuptools

setuptools.setup(
    name='SCE-CLI-SocietyOfComputerEngineers-SJSU',
    version='1.0.0',
    author='bred',
    description='sce project manager',
    url='https://github.com/SCE-Development/SCE-CLI',
    package_dir={'':'src'},
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'sce = sce:cli'
        ],
    },
)
