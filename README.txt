This file is for you to describe the DanieleChallenge application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``DanieleChallenge`` using easy_install::

    easy_install DanieleChallenge

Make a config file as follows::

    paster make-config DanieleChallenge config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

This contains a MySQL Schema database stored in a file called : testDaniele.db.sql
So, it's important to change the user && password --credentials-- to connect to your own mysqld (server)
To do this please follow this instructions:

	1.- Open controllers/formtest.py and edit the dns connection string
		ie: mysql://user:password@localhost/testDaniele?charset=utf8&use_unicode=0', pool_recycle=3600
		Edit this line in the file mentioned with your own credentials.

	2.- Connect to your MySQL database engine and type :
		mysql_shell>> source testDaniele.db.sql
		this should be enough to have the database schema to run this application.
 
Then you are ready to go.

Once you're in your webserver please see this using: http://yourServer_dns_or_ip/~yourInstalationPath/formtest/index 

Thanks

xOCh
