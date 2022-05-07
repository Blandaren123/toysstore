# Toy Store

[Live application can be found here](https://toysstore-udd.herokuapp.com/)

# Purpose of the project

The purpose of this page is for travelers to post their tips or tell about their travels.
In a community, people can comment and plan their next vacation by posting where they want to go
Or give advice based on places they've visited
In other words, it's like a traveling community

# User stories
Here is Kanban for user story [here](https://github.com/Blandaren123/Django.P4/projects/2)

1. As a Site user/ admin I can like or unlike post so That i can see what i like or unlike
2. As a Admin I can Access my adming panel so That i can manage posts and comments
3. As a User/Admin I can Delete Posts/comments so That i can delete post or comments if i regret
4. As a User I can Click on a post so That I can View the deatails
5. As a User I can create an account so That i Can Interact with other users or comment
6. As a User/admin I can write html code so That get better styling in Post
7. As a User I can only edit or delete my own post so That nobody can delete or edit my own post
8. As a user I can edit my profile so That All my data is correct
9. As a user I can change password so That if i want a new password i change
10. As a User I can sign up/log in and comment so That other can see and up or down vote

# Databases
Easy sign up and posting for a blog community


![image info](/static/images/Datamodels.png)

# Wireframes
![image info](/static/images/wirframemo.PNG) ![image info](/static/images/wurreframewin.PNG)

With a design that follows through the theme of simplicity, the pages are divided by bootstrap columns and rows, and the layout is kept consistent so that the user feels at ease at all times.

# Features
- __Navigation Bar__
  * The navigation bar is fully responsive, allowing users to navigate easily.
  * A fast and easy way to register and log in.
  * Design with easy color and minimalist style.
  * The navbar changes to add posts, edit profiles, and logout once you are logged in

![image info](/static/images/navbars.PNG)

- __Add Post__
  * Minimal post additions

![image info](/static/images/post.PNG)

- __Comments__
  * Everyone can comment easily and quickly
 

![image info](/static/images/comments.PNG)

- __Click to View__
  * Simply click a post to open it and read it

![image info](/static/images/clicker.PNG)


# Futures implement
  * A picture gallery section with inspiration for different places
  * An online booking system to book Vacation.

# Typography and color scheme
- Color: white, gray and almost pink background

# Technology
- Wireframes for layout on desktop and mobile in Balsamiq tools.
- This site was laid out and structured using HTML, Python, Javascript, Django
- Style and appearance using CSS.
- Use Github to deploy the project and read the README.
- Gitpod is used for coding.
- CodeInstuite project, YouTube, and Google for tutorials and troubleshooting.
- Skype for contact with the mentor for tips and advice. 
- jigsaw, W3c and lighthouse for testing and troubleshoot.


# Testing
- ## I Used manual testing for this Project

- I tested this side on Microsoft edge and Chrome and it seems to works great.
- The page is viewable on desktops, iPads, and phones when I tested.
- I can confirmed All sections such as the navigation bar section are operational and easy to use.

- ## As Guest 
- Can enter post and comments with name.
- click to view the post.

- ## As Registered and Logged in User
- Can like a post
- Can change and edit your own Post
- Can Edit profile and Change password

- ## Test Person 
- let my Friends and family test to see if it works as it should.


- __Bugs__
- Wrote templates wrong when so it doesnt find the files

![image info](/static/images/bug.PNG)

- Write Templates on the right way
- solving with this 

![image info](/static/images/bugfix.PNG) worked fine

# Validator Testing 

## HTML and CSS
- No Error on the official 


![image info](/static/images/Wc3.PNG)


## Accessbility
- It's confirmed that the colors and fonts chosen are readable in devtools when tested through Lighthouse

![image info](/static/images/lighthouse.PNG)


## Python
- Pep8 test
Had only lines to long nothing more

![image info](/static/images/pep8test.PNG)

# Unfixed Bugs
Yes i have this on site that i cant fix in Edit Profile

![image info](/static/images/Buuugs.PNG)

# Deployment
I used Gitpod to develop the project. I contributed all changes to git version control, and I saved changes to GitHub using the push command in Gitpod.

## Heroku
Ensure your project has these two files before building a Heroku app: requirements.txt - This is created by pip3 freeze --local > requirements.txt Procfile - This is created by echo web: python run.py > Procfile

## Setting up deployment
- DATABASE_URL must be added to settings.py temporarily:
- To migrate the database models in the project to the Postgres database, run the following command: python3 manage.py migrate
- check git.ignore if env.py is there
- If you want your Heroku app to be deployed directly from a Github repository, you can do so as follows: On the deploy tab of your Heroku app, select GitHub - Connect to GitHub. If not already logged in, sign up with GitHub. We will then prompt you to find a Github repository to connect to.

- To deploy your app to Heroku click the "Deploy Branch" button.


# Credits
## Contents
- Bootsraps was taken from [here](https://getbootstrap.com/)
- youtuber tutorial [here](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).
- Slacks for some bug fixes
- Cloudinary [here](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=483362991544&utm_term=cloudinary&gclid=Cj0KCQiA95aRBhCsARIsAC2xvfwkb-wCh-OYhKE-Xy-ND5gOUxKzbTvIo_3zJCxu0V9aNLUKTfFftl4aAjqTEALw_wcB). for easy upload

## Media
- some Post picture was taken from [pexels](https://www.pexels.com/sv-se/)

# Acknowledgements
- my mentor, I receive support, advice, and feedback.
- Slack for all the help with Bug and advice
- Friends and Family that test it