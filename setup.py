from setuptools import find_packages,setup

setup(
    name = 'face_check',
    version = '0.1',
    packages = find_packages(),

    install_requires=['face_recognition>=1.2',
                      'numpy>=1.15',
                      'opencv-python>=3.4',
                      'requests>=2.21'
                      ]
)