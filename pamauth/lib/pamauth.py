#pamauth.py

"""
Uses PAM to check authenticate the user. 

Validates the user credintentials with PAM and checks 
if the user has sudo rights on the server. If there is no existing user 
in the server database one will be created with the same creditentials. 
If user has sudo rights, they will be included in the website functions.

"""

import pam, grp
from django.contrib.auth.models import User, Group

# check if the user is authenticated from the system
def pam_authenticate(username=None, password=None):
	if pam.authenticate(username, password, service="login"):
		try:
			user = User.objects.get(username=username)

			# Change user password in DB because PAM authenticated the new one.
			if user.check_password(password):
				return True

			user.set_password(password)
			user.save()

			return True

		except User.DoesNotExist:
			# New user that is not in the database.
			user = User.objects.create_user(username=username, password=password)
			
			# Checks if the user has sudo right for the server
			if username in grp.getgrnam("sudo")[3]:
				if not "sudo" in Group.objects.all():
					group = Group.objects.create(name="sudo")
				else:
					"Found group sudo."
					group = Group.objects.get(name="sudo")

				print 'Made user %s sudoer' % username
				user.groups.add(group)
				user.save()
		
			return True

	return False