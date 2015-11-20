Title: Working with packages whilst developing
Date: 2015-11-20 12:15
Author: niceguydave
Category: Web development
Tags: python, django
Slug: developing-with-packages
Status: draft

One of the beauties of working with open source software in general and Python in particular is making use of the
abundance of software packages to make development more effective.

Sometimes, however, there are issues which crop up which make it impossible to simply `pip` install a package.  A
couple of examples I've come across over the last few months

+ Storage of media is always assumed to be local i.e. uploading to, say, S3 isn't taken into account
+ There's a bug in the version of a package I'm using. A fix has been merged into the latest release of the package but
  not into the branch I'm forced to use because of other dependencies.

Although it makes sense to stick to using `pip` version, sometimes it's just not possible and I have to fork the project
to make changes.


## Making local changes to this package

Let's start with a simple example.  One of the fields I want to use in a package I'm working with only lets me store
200 characters in a URL field - I would like to store 300.  The standard procedure here would be to trigger a schema 
migration and then apply this.  If I want this change to be picked up by my package, though and to push this change 
back up to the project source, how should I do this?  The code is stored somewhere in my virtual environment and is 
sand-boxed from being modified

