from tools.setup import SceSetupTool

setup = SceSetupTool()
setup.check_os()
setup.check_installation("docker", "docker --version", "https://docs.docker.com/desktop/")
setup.check_installation("mongo", "mongo --version", "https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials")
setup.setup_rpc()
setup.check_directory("Core-v4")
setup.check_directory("SCE-discord-bot")