# tasks to be run by the invoke tool

from invoke import task, run

@task
def clean():
    print("Removing output slides")
    run('rm reveal.html')

@task('clean')
def slides():
    print("Creating Slides Based on reveal.js")
    run('rst2html5 --jquery --reveal-js --pretty-print-code --embed-content --pygments --reveal-js-opts theme=sky source/index.rst > output/index.html')
    run('cp source/_static/* output/')

@task('slides')
def serve():
    print('Starting Web Server')
    run('python -m SimpleHTTPServer')

@task('slides')
def publish():
    print('Publishing to github pages')
    run('ghp-import -p output')
