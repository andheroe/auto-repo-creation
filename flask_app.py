
# Flask app which accepts a github username and public access token,
# creates a new repository on the user's github page, and pushes its own
# code from the server to the github repository

from flask import Flask, request
import githubfuncs
import github

app = Flask(__name__, static_folder='', static_url_path='')
# app.debug = True

@app.route('/')
def display_form():
    # display form for input of the github username and token
    return app.send_static_file('index.html')

@app.route('/pushtogithub', methods=['POST'])
def push_to_github():
    # get the github username and token, create a new repository on github,
    # and push the files from the server to the github repository
    github_username = request.form['username']
    github_token = request.form['token']
    # test_message = 'Your username is ' + github_username + '.  Your token is ' + github_token + '.'
    try:
         githubfuncs.create_remote_repo(github_token)
    except github.GithubException as error:
        if error.__class__.__name__ == 'BadCredentialsException':
            return (
                'Authentication failed.  Please check your Github personal access '
                'token.'
                )
        elif error.data['message'] == 'Repository creation failed.':
            return(
                'The auto-repo-creation repository already exists on your Github '
                'page.'
                )
        else:
            # err_type = error.__class__.__name__
            return 'An error occurred.  Please try again.'
    try:
        githubfuncs.push_code(github_username, github_token)
    except Exception as error:
        # delete the auto-repo-creation repo that was created by this program
        # in the previous step to allow the user to re-run the program without getting the
        # 'repo already exists on your page' error
        g = github.Github("<token>")
        repo = g.get_repo(full_name="auto-repo-creation")
        repo.delete()
        return (
            'An error occurred while pushing the code with git.  Please try '
            'again.'
            )
    exit_message = 'The code has been pushed to '+ github_username + '! Please check your github page.'
    return exit_message

