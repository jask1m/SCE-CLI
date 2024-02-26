#!/bin/bash

_sce_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="clone run link setup completion"
    repos="Clark cleezy Quasar SCE-discord-bot SCEta"

    if [[ ${prev} == "clone" || ${prev} == "run" || ${prev} == "link" ]] ; then
        COMPREPLY=( $(compgen -W "${repos}" -- ${cur}) )
        if [[ ${#COMPREPLY[@]} -eq 0 ]]; then
            COMPREPLY=( $(ls) )
        fi
        return 0
    fi

    if [[ ${cur} == * ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        if [[ ${#COMPREPLY[@]} -eq 0 ]]; then
            COMPREPLY=( $(ls) )
        fi
        return 0
    fi
}
complete -F _sce_completion sce