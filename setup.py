from setuptools import setup, find_packages

setup(
    name="potracer",
    version="0.0.4",
    description="Python Potrace",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/tatarize/potrace",
    license="GPLv2+",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "Pillow",  # Asegúrate de incluir cualquier otra dependencia necesaria
    ],
    extras_require={
        'cli': ["potrace-cli"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Utilities",
    ],
    zip_safe=True,
    include_package_data=True,
)
