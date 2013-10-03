# tasks to be run by the invoke tool

from invoke import task, run

@task
def clean():
    print("Removing output slides")
    run('rm reveal.html')

@task('clean')
def slides():
    print("Creating Slides Based on reveal.js")
    run('rst2html5 --jquery --reveal-js --pretty-print-code --embed-content --pygments networking101/source/index.rst > reveal.html')

@task('slides')
def serve():
    print('Starting Web Server')
    run('python -m SimpleHTTPServer')
