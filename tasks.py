from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/ui/ui.py", pty=True)
    # At the moment this only runs the ui.py file because i haven't created 'index.py'

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)