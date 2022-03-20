import subprocess

"""
The below function checks the status of Docker on the user's computer. There
are three situations:
1. Docker is installed and the daemon (e.g. docker desktop) is running
2. Docker is installed and the daemon is not running
3. Docker is not installed

This function handles each case across Windows and Unix systems so in case
docker is unable to be ran, a helpful error is presented to the user.
"""
def check_docker_status():
  try:
    subprocess.run(
      ['docker', 'ps'],
      check=True,
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL
    )
    # Case 1, Docker is installed and the daemon isn't running
    return { 
      'is_installed': True,
      'is_running': True
    }
  except FileNotFoundError:
    # Case 2, Docker is not installed
    return { 
      'is_installed': False,
      'is_running': False
    }
  except subprocess.CalledProcessError:
    # Case 3, Docker is installed but the daemon isn't running
    return {
      'is_installed': True,
      'is_running': False
    }

"""
this method continually prompts the user to enter a "valid" input. 
validator should be a one argument function which returns a Boolean 
(whether the input is valid or invalid)
Returns:
    the valid user input
"""
def prompt_user(prompt, validator):
    ans = input(prompt)
    while not validator(ans):
        ans = input(prompt)
    return ans

"""
abstraction on top of prompt_user() to prompt for yes or no.
"""
def prompt_user_yn(prompt):
    return prompt_user(prompt, lambda inp: inp == 'y' or inp == 'n')


