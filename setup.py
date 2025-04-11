from setuptools import setup, find_packages

setup(
    name="sonic_nova",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pyaudio',
        'pytz',
        'python-dotenv',
        'aws-sdk-bedrock-runtime',
        'smithy-aws-core'
    ],
    python_requires='>=3.7',
) 