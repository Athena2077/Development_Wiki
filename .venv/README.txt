
************************************************************************************************************************************
About

This webapp is to be used for development teams to post information about internal practrices.

For exmaple, if the development team uses a third party softeware to creat bespoke solutions, this webapp can be used to post information about the softeware and common code used by the dev team.
This can help new devs or users of the software understand the teams practices.

It can also be used to offer suggestions into the lastest codign practices, where to find goo programming podcasts/tutorials and other information. 

This app has a cagtegories databse in which users can add new categories to choose when posting information. 
Categories can also be used to filter posts, the posts can also be filtered on the author and are presented in lastest date first. 

************************************************************************************************************************************
Permission Information

Standard User - Can view all posts, create/update their own posts, create/update the categories list, edit their profile information. New users default as standard users.

Admin User - Can view all posts, create/update/delete their own posts, update/delete other users posts, create/update/delete the categories list, edit their profile information.
                Admin users can access the Admin page and make changes to the database and users directly, using the /admin url path.

************************************************************************************************************************************
Users

Admin -
    Username:       sysAdmin
    Email (fake):   sysAdmin@email.com
    Password:       P@$$w0rd!

Standard User 1 -
    Username:       TestUser
    Email (fake):   TestUser@email.com
    Password:       testing321

Standard User 2 -
    Username:       TestUser2
    Email (fake):   TestUser2@email.com
    Password:       testing000

************************************************************************************************************************************
Resetting Password

To use this feature a real email will need to be used and linked to the user profile.
Profile information can be changed using the profile page (link in nav bar and mini menu), if the user is signed into the app.
The profile information can also be changed through the admin page (admin only).

************************************************************************************************************************************
Filter Options

Posts can be filtered on the Post Username or Category, these filters can be seen on the top of the Index(Home) page as drop down buttons.
You can also click on the suername/category on the psot to take you to the filter page(s).

************************************************************************************************************************************
Other 

posts.json contains dummy post data, used to quick import into database using python shell commands

************************************************************************************************************************************
Cat Profile Photo:

https://www.freepik.com/free-vector/cute-cat-gaming-cartoon_13486463.htm#query=avatar&position=7&from_view=search

Image by catalyststuff on Freepik

************************************************************************************************************************************