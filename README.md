# Toy Store
![image info](/media/responsive1.PNG)

[Live application can be found here](https://toysstore-udd.herokuapp.com/)



![image info](/media/fbsocial.PNG)

[facebooksite](https://www.facebook.com/Toysstore-111655058205295/?ref=pages_you_manage)

# Purpose of the project

Basically, this is an e-commerce site that sells mostly toys, but also a few other kid-related products.


Users are free to create accounts or just buy without one, and admin have full access to the site as a site owner

Users can test the card by entering 4242 4242 4242 4242 - and at the end, a 5-number postal code can be entered.

# User stories
Here is Kanban for user story [here](https://github.com/Blandaren123/toysstore/projects/1)

1. As a Owner I can Add, Edit and Remove product so That Easy to take out old and add new stuff
2. As a Siteuser I can search in the searchbar so That it's easy to find what i searchs for
3. As a siteuser I can rate so That people know if how good or bad this products is
4. As a Siteuser I can select size so That i can fins the best size to buy
5. As a admin/siteowner I can delete product so That if i dont want it in my shop
6. As a Buyer I can get confirmation mail when i purchase so That i know the purchase was done
7. As a Admin/siteowner I can remove users so That if it gets to much accounts
8. As a User I can my billing adress so That i odnt have to enter again
9. As a User/buyer I can add in the shopping cart so That it's easy to buy more fast
10. As a User I can click on site's facebooks business page so That I Can Follow Them
11. As a Admin I can add product so That if i want to add new product in the shop
12. As a User I can Register an Account so That I Can Have a personal account with my profile
13. As a User I can Login or logout so That I can Access My account
14. As a site user I can view the policy so That user know what policy the site have
15. As a User I can Recover my password so That i can access my again if I lost my password
16. As a Buyer I can View the products so That I can select some to Purchase
17. As a Buyer I can View Product individual details so That I can see the price, description of the product and product image
18. As a Buyer I can See how much i have in my shopping bag so That i can see how much everything in total and what product i have put in
19. As a User I can register for newsletter so That I can recieve news on products or campaigns
20. As a Admin I can **add, edit and remove ** so That i can add new products, edit them or delete it


# Databases
Easy-to-use ecommerce site 


![image info](/media/datastrucctures1.PNG)

# Wireframes
![image info](/media/wireframesdesk.PNG) ![image info](/media/wireframesphone.PNG)

Following the theme of simplicity, the pages are divided by bootstrap columns and rows, and the layout stays consistent so that the user feels at ease at all times.

# Features

- __Navigation Bar__
  * The navigation bar is fully responsive, allowing users to navigate easily.
  * A fast and easy way to register and log in.
  * Design with easy color and minimalist style.
  * The navbar menu changes to dropdown when it is smaller screen

![image info](/media/nav1desk.PNG)

![image info](/media/nav1desk2.PNG)

![image info](/media/navphone.PNG)


- __Categories__
  * Categories with easy-to-filter products

![image info](/media/kategories1.PNG)

- __Home__
  * Buy now button for fast buy
  * Social link for Facebook
  * Subscribe if you want news letter

- __About__
  * Little about the page.

- __Add to Bag__
  * It's easy to add and buy both for those who have signed up and those who haven't

- __Shopping Bag__
  * The shopping bag shows how much you have added, or you can click it for more information

- __Popup message__
  * Throughout the site, you will see a pop-up message or alert

- __404 error__
  * Made 404 page 
![image info](/media/404page.PNG)



# Futures implement
  * A system to keep track of how many products you have and when something is out of stock
  * A comment system so people can give comment about the products

# Typography and color scheme
- Color: white, black and big backgorund for homepage

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

- ## As Guest/Anonym user
- News and campaigns about products can be subscribed to
- Click and view products and fast buy
- Mail sent with orderdetail what you have purchase
- Can read about me page

- ## As Registered and Logged in User
- Can edit profiles
- Can change password
- Can Edit profile and Change password
- See Order history
- Set default Delivery informations

- ## As Admin/siteowner
- Can delete products
- Can Edit products
- Can Add products
- Delete user
- Add new categories

- ## Test Person 
- let my Friends and family test to see if it works as it should.
- I have tested too and everythings seems to work fine

# Bugs
- No Nugs wehre found


# Validator Testing 

## W3C HTML
- html validator no error
![image info](/media/htmlvalidator.PNG)

## w3C Jigsaws
- base css no error
![image info](/media/basecss.PNG)

## Accessbility
- It's confirmed that the colors and fonts chosen are readable in devtools when tested through Lighthouse

![image info](/media/lighthouse.PNG)


## Python
- flake8 test
Had only lines to long nothing more


# Unfixed Bugs

- Only line longer then 50 character

# Other Services

## stripe
  Stripe was used to take payments for this online store; you need to create a Stripe account first and then add the HTML, Python, JS, and other code you need to implement your needs in their documentation.
  For setup[link](https://stripe.com/docs/payments/quickstart)
  Here is the setup in Settings.py
   ![image info](/media/stripe.PNG)

## AWS3
Using Amazon AWS S3, I store all static and media files for this site. I created a bucket, user group, and user that have access to this site and its files. In order for the files to be correctly served the following settings have to be added to your main settings.py file.
here is the setup in settings.py
![image info](/media/AWS3.PNG)


## Mailship
Was used to create the newsletter signup form. so i can get subscriber

## Facebook
- Business page was created on [Facebook](https://www.facebook.com/Toysstore-111655058205295/?ref=pages_you_manage)

## GDPR privacy policy generator
- For policy

## Gmail SMTP
I used Gmail SMTP to send confirmation emails and all allauth related emails.
I Used This [links](https://kb.synology.com/en-global/SRM/tutorial/How_to_use_Gmail_SMTP_server_to_send_emails_for_SRM) for setup
setups in settings.py
![image info](/media/gmail.PNG)


# Deployment

## Github and Gitpod
1. Access your Github Account and look for [Code-institute-templace](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click the "Use this template" button beside the green button that says "Gitpod".
3. Add repository name and description(optional).
4. Click the Create repository from template.
5. now you can click on the green Gitpod button when the repository hade been created.
6. It is best to open the workspace from Gitpod (rather than Github) to open your previous workspace rather than creating a new one when working on a project
7. dont forget to pin in Gitpod so the workspace wont get deleted.
8. Committing your work often and using clear/explanatory messages is recommended; you can do this using the following commands:
- git add .: adds all modified files to a staging area
- git commit -m "A message explaining your commit": commits all changes to a local repository.
- git push: pushes all your committed changes to your Github repository.

## Forking Github Repository
#### To clone or Fork repository
1. Find/Access your or relevant Github repository
2. Clock on "Fork" on the top right of the page
3. Your repository has now been "Forked" and you will find a copy of the repository in your Github account.


## Heroku
#### This application has been deployed from Github to Heroku
1. create an account or log in if you are registered already [Heroku](https://dashboard.heroku.com/apps)
2. Create a new app, add the app name and your region and click on create app.

#### You can create the files required for Heroku to install your project dependencies by typing pip3 freeze --local > requirements.txt in the Gitpod CLI. Please note this file should be added to a .gitignore file to prevent the file from being committed. A Procfile is also required that specifies the commands that are executed by the app on startup.

#### because of security breach on Heroku, you have to use this command below to connect and deploy to Heroku.
1. Login to Heroku via CLI using: heroku login -i
2. Enter your Heroku email and password
3. Connect to the Heroku git remote using: heroku git:remote -a <YOURHEROKUAPPNAME>
4. when you deploy you need to type: git push heroku main.

#### Heroku Settings Environments Variables 
- In settings tab and click Reveal Config vars and set following:
![image info](/media/configvar.PNG)

# Credits
## Contents
- Bootstraps was taken from [here](https://getbootstrap.com/)
- Took the most of the codes from Code in institue, botique ado project followed it and made some change
- Slacks for some help when i had some problem
- Ubuy for some pictures and describtions [here](https://www.ubuy.com.se/en/)
- H&M for describtions [here](https://www2.hm.com/en_gb/index.html)


## Media
- some Post picture was taken from [pexels](https://www.pexels.com/sv-se/)

# Acknowledgements
- my mentor, I receive support, advice, and feedback.
- Slack for all the help and advices
- Friends and Family that test it