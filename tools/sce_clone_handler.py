import subprocess

class SceCloneHandler:
	project_names = {
		"core-v4": "https://github.com/SCE-Development/Core-v4.git",
		"sce-discord-bot": "https://github.com/SCE-Development/SCE-discord-bot.git",	
		"discord-bot": "https://github.com/SCE-Development/SCE-discord-bot.git",
		"quasar": "https://github.com/SCE-Development/Quasar.git"
	}

	def __init__(self, projects):
		if projects == None:
			self.projects = ["core-v4"]
		self.projects = projects

	def print_usage(self):
		print(f"""
		Please enter at least one valid project.
		Valid projects are: {list(self.project_names.keys())}.
		""")

	def invalidName(self, project):
		print(f"""
		\"{project}\" is not a valid project name.
		Valid projects are: {list(self.project_names.keys())}.
		""")

	def handle_cloning(self):
		if not self.projects:
			self.print_usage()
			return
		for project in self.projects:
			if project.lower() not in list(self.project_names.keys()):
				self.invalidName(project)
			else:
				process = subprocess.Popen(['git', 'clone', self.project_names[project.lower()]])
				process.communicate()