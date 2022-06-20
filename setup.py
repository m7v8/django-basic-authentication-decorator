import setuptools


setuptools.setup(
    name='django-basic-authentication-decorator',
    version='0.9',
    license='BSD',
    description='Decorator to provide Basic Authentication for Django Views',
    url='https://github.com/m7v8/django-basic-authentication-decorator',
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    py_modules=['django_basic_auth'],
    include_package_data=True,
)
