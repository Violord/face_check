from setuptools import find_packages,setup

setup(
    name = 'face_check',
    version = '0.1',
    author= 'Violord',
    author_email= 'hy19930816@163.com',
    description= 'A small function that compares faces.',
    license= 'MIT',
    url= 'https://github.com/Violord/face_check.git',
    packages = find_packages(),

    install_requires=['face_recognition>=1.2',
                      'numpy>=1.15',
                      'opencv-python>=3.4',
                      'requests>=2.21'
                      ]
)