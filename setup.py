import setuptools
import os, glob

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version():
    import os
    vf = 'version.txt'
    maxversions = [9, 9, 9, 9, 9, 9, 9]

    def add_version(version, index=-1):
        if index == -1: index = len(version) - 1
        version[index] += 1
        if version[index] > maxversions[len(version) - index - 1]:
            version[index] = 0
            if index == 0:
                raise Exception('Max version number reached. %s' % (version))
            return add_version(version, index - 1)
        else:
            return version

    if not os.path.exists(vf):
        raise Exception('version.txt not found or  is invalid')
    # f=open(vf,'w')
    # f.write(str(249))
    # f.close()
    with open(vf, 'r') as f:
        numbers = f.read().strip()
        if numbers == '':
            raise Exception('version.txt not found or  is invalid')
        version = numbers.split('.')
        version = [int(x) for x in version]
        version = add_version(version)
        version = '.'.join([str(x) for x in version])

    with open(vf, 'w') as f:
        f.write(version)
    return version

packages=setuptools.find_packages(exclude=['local','local.*'])

print('packages:', packages)

version = get_version()
print("version:", version)
setuptools.setup(
    executable=True,
    name="freehub",  # Replace with your own username
    version=version,
    author="WangPei",
    author_email="1535376447@qq.com",
    description="With one command, upload file to freehub , or download from freehub. Easy to use. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/Peiiii/freehub",
    packages=packages,
    package_dir={'freehub': 'freehub'},
    install_requires=[
        'dulwich',
        'fire'
    ],
    entry_points={
        'console_scripts': [
            'freehub = freehub.clitools.cli:main',
        ]
    },
    include_package_data=True,
    package_data={
        'freehub': [
            'data/*', 'data/*/*', 'data/*/*/*', 'data/*/*/*/*', 'data/*/*/*/*/*', 'data/*/*/*/*/*/*',
            'data/*/*/*/*/*/*/*',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)