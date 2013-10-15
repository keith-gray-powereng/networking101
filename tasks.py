# tasks to be run by the invoke tool

from invoke import task, run

import os.path

@task
def clean():
    print("Removing output slides")
    if os.path.exists('output'):
        run('rm -R output')

@task('clean')
def slides():
    print("Creating Slides Based on reveal.js")
    if not os.path.exists('output'):
        run('mkdir output')
    run('rst2html5 --jquery --reveal-js --pretty-print-code --embed-content --pygments --reveal-js-opts theme=sky source/index.rst > output/index.html')
    if os.path.exists('source/_static'):
        run('cp source/_static/* output/')

@task('slides')
def serve():
    print('Starting Web Server')
    run('python -m SimpleHTTPServer')

@task('slides')
def publish():
    print('Publishing to github pages')
    run('ghp-import -p output')
