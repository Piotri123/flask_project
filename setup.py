from setuptools import setup

setup(
    name="markdown blog",
    version="0.1",
    long_description="MarkDown blogging platform",
    packages=["mdblog"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "celery==5.1.2",
        "Flask==2.0.3",
        "Flask-SQLAlchemy==2.5.1",
        "Flask-WTF==1.0.1",
        "email-validator==1.3.1"
    ]
)