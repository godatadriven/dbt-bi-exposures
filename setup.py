from setuptools import setup, find_packages


requirements = ["dbt-core==1.1.0"]
setup_requirements = ["pytest-runner"]
tests_requirements = ["pytest==5.4.1"]
dev_requirements = [
    "pre-commit==2.19.0",
    "flake8==4.0.0",
    "black==22.3.0",
    "bump2version",
] + tests_requirements
extras_requirements = {"dev": dev_requirements}
setup(
    name="dbt-bi-exposures",
    version="0.1",
    # Author details
    author="Guillermo Sanchez, Jovan Gligorevic",
    author_email="guillermosanchez@godatadriven.com, jovangligorevic@godatadriven.com",
    packages=find_packages("dbt_bi_exposures"),
    package_dir={"": "dbt_bi_exposures"},
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=tests_requirements,
    extras_require=extras_requirements,
)