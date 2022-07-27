#!/bin/bash

function print_repo_nicknames {
    echo
    echo "each repo has nicknames:"
    echo "Core-v4:core-v4, corev4, cv4, c4, c"
    echo "Quasar:quasar, q, idsmile"
    echo "SCE-discod-bot:sce-discord-bot, discord-bot, discord, bot, d"
}

function print_usage {
    echo "usage: sce {clone,run,link,setup} {repo name}"
    echo
    echo "clone: clone the given repo from github."
    echo "run: run the repo using docker"
    echo "link: tell the sce tool where to find the repo on your computer"
    echo "setup: copy config.example.json in a repo to config.json"
    print_repo_nicknames
}

SCE_COMMAND_DIRECTORY=$(echo $0 | rev |  cut -c7- | rev)
GITHUB_BASE_URL="https://github.com/SCE-Development/"
COREV4_REPO_NAME="Core-v4"
QUASAR_REPO_NAME="Quasar"
SCE_DISCORD_BOT_REPO_NAME="SCE-discord-bot"

COREV4_NAMES=("core-v4" "corev4" "cv4" "c4" "c") 
QUASAR_NAMES=("quasar" "q" "idsmile")
SCE_DISCORD_BOT_NAMES=("sce-discord-bot" "discord-bot" "discord" "bot" "d")

VALID_COMMANDS=("link" "clone" "run" "setup")

function contains_element {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

function is_quasar_alias {
    result=$(contains_element "$1" "${QUASAR_NAMES[@]}")
    return $result
}

function is_corev4_alias {
    result=$(contains_element "$1" "${COREV4_NAMES[@]}")
    return $result
}

function is_discord_bot_alias {
    result=$(contains_element "$1" "${SCE_DISCORD_BOT_NAMES[@]}")
    return $result
}

function is_valid_command {
    result=$(contains_element "$1" "${VALID_COMMANDS[@]}")
    return $result
}

is_valid_command "$1"
if [ $? -eq 1 ] 
then  
    print_usage
    exit 1
fi

name=""
is_quasar_alias "$2"
if [ $? -eq 0 ]
then
    name=$QUASAR_REPO_NAME
fi

is_corev4_alias "$2"
if [ $? -eq 0 ]
then
    name=$COREV4_REPO_NAME
fi

is_discord_bot_alias "$2"
if [ $? -eq 0 ]
then
    name=$SCE_DISCORD_BOT_REPO_NAME
fi

echo $name