from setuptools import setup, find_packages

setup(
    name='django-cache-throttle',
    version='2012.11.09.3',
    description='Cache-based rate-limiting for Django.',
    long_description='Uses Django\'s caching framework to provide a view decorator that rate limits through a regenerative stamina indicator.',
    author='Brad Beattie',
    author_email='bradbeattie@gmail.com',
    url='https://github.com/bradbeattie/django-cache-throttle',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data = { '': ['README.md'] },
    install_requires=['django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
