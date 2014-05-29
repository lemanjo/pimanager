#is_sudo.py

def is_sudo(user):
	return user.groups.filter(name='sudo')