WEB APPLICATION

This Python flask web application is meant to be easily copied to a user's own pythonanywhere.com website.  It enables a Github user to automatically create a repository called 'auto-repo-creation' with the web application code on his or her Github page.  Then, the user can clone the 'auto-repo-creation' repository to his or her own pythonanywhere.com server.  After following the installation steps below, the user will have re-created this web application on his or her own pythonanywhere.com website.

To create the Github repository, the user must first create a Github personal access token with 'public_repo' scope.  This allows the web application access to the user's public respositories in order to push the web application code.  On the website home page, the user enters his or her Github username and personal access token and clicks the 'Create Repo' button to push the repository.


INSTALLATION

-Sign up for a free pythonanywhere account at www.pythonanywhere.com.

-Click to create a Webapp using Flask and Python 3.7.

-Click to open a Bash console and configure git with your email address and name by running the following  commands:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

-Then, run:

git clone [url of your Github repository]
(example: git clone https://github.com/mygithubusername/auto-repo-creation.git)

-Within the mysite directory, open the config.py file and change the PY_ANYWHERE_USERNAME to your pythonanywhere username.

-In the Bash console, run the following command:

cd auto-repo-creation

Then, run:

virtualenv venv --python=python3

-From the pthonanywhere dashboard (click the icon in the upper left hand corner of the screen), go to your web app, and make the follwoing changes:

1) Under Code, change the Source Code path to /home/[pythonanywhereusername]/auto-repo-creation
2  Under Code, click into the WSGI configuration file and change the project home value to u'/home[pythonanywhereusername]/auto-repo-creation'
3) Under Virtual Environment set the path to the virtual environment (/home/[pythonanywhereusername]/auto-repo-creation/venv), reload the web application, and click to start a new console in the virtual environment

-Then, in the new Bash console (you should see (venv) at the left of the command prompt), run the following command:

pip install -r requirements.txt

The pip installation may take a couple of minutes.

-Once the installation is complete, from the dashboard, go into your Webapp and click Reload.

-When you visit your pythonaywhere homepage (yourpythonanywhereusername.pythonanywhere.com), you should see a copy of the original website!