import nox


@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    session.install(".")
    session.install("pytest", "pytest-asyncio")
    session.run("pytest", "tests")


@nox.session
def format(session):
    session.install("black")
    session.run("black", "src", "tests")


@nox.session
def check_format(session):
    session.install("black")
    session.run("black", "--check", "src", "tests")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "src", "tests")


@nox.session(python=["3.10", "3.11", "3.12"])
def coverage(session):
    session.install(".")
    session.install("pytest", "pytest-asyncio", "coverage", "pytest-cov")
    session.run(
        "pytest",
        "--cov=src/api_football_sdk",
        "--cov-config=coverage.ini",
        "--cov-report=term",
        "--cov-report=html",
        "tests",
    )
