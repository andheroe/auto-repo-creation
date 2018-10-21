from config import PY_ANYWHERE_USERNAME
from github import Github
import pexpect
import time

def create_remote_repo(github_token):
    # accepts the user's github token and uses the pygithub api to create a
    # new remote github repository
    g = Github(github_token)
    user = g.get_user()
    user.create_repo('auto-repo-creation')


def push_code(github_username, github_token):
    # pushes files from the local git repository on the server to the
    # auto-repo-creation remote repository
    my_bash = pexpect.spawn('/bin/bash', cwd='/home/' + PY_ANYWHERE_USERNAME + '/auto-repo-creation')
    my_bash.delaybeforesend = 1
    my_bash.sendline(
        'git remote set-url origin https://github.com/' + github_username +
        '/auto-repo-creation.git')
    my_bash.delaybeforesend = 1
    my_bash.sendline('git add .')
    my_bash.delaybeforesend = 1
    my_bash.sendline("git commit -m 'populate repo'")
    my_bash.delaybeforesend = 1
    my_bash.sendline('git push -u origin master')
    my_bash.expect("Username for 'https://github.com':")
    my_bash.delaybeforesend = 1
    my_bash.sendline(github_username)
    my_bash.expect("Password for 'https://" + github_username + "@github.com':")
    my_bash.delaybeforesend = 1
    my_bash.sendline(github_token)
    time.sleep(10)


