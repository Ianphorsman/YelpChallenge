from setuptools import setup

setup(
    name='YelpChallenge',
    description="Analysis of Yelp Dataset",
    url="https://github.com/Ianphorsman/YelpChallenge",
    author='Ian Horsman',
    author_email='ianphorsman@gmail.com',
    license='MIT',
    version='0.1.0',
    packages=['yelp_challenge'],
    install_requires=['numpy', 'tensorflow-gpu', 'pandas']
)