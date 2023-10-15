import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='scrubber',
        version='1.0.0',
        license='MIT License',
        url='https://github.com/nirmalparmarphd/scrubber',
        description='Data scrubbing and cleaning library', 
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Nirmal Parmar, PhD',
        author_email='nirmalparmarphd@gmail.com',
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=['scikit-learn','numpy','pandas','scipy', 'matplotlib', 'seaborn', 'openpyxl', 'pyspark'],
        zip_safe=False)