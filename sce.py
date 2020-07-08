from tools.setup import SceSetupTool
import threading

setup = SceSetupTool()
setup.check_os()
setup.check_docker()
setup.check_mongo()

setup.setup_rpc()

t1 = threading.Thread(target=setup.setup_core_v4, args=())
t2 = threading.Thread(target=setup.setup_discord_bot, args=())

t1.start()
t2.start()

t1.join()
t2.join()


"""
setup.setup_rpc()
setup.setup_core_v4()
setup.setup_discord_bot()
"""


