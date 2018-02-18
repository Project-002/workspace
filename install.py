import json
import os
from subprocess import call

def main():
    workspace = json.load(open('./002.code-workspace'))

    for repository in workspace['folders']:
        repo = repository['path']
        if not os.path.exists(repo):
            print(f'Closning {repo}')
            call(['git', 'clone', f'https://github.com/Project-002/{repo}.git', repo])

if __name__ == '__main__':
    main()
