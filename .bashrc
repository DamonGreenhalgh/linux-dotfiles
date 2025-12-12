#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='\e[36m\u\e[0qm@\e[36m\h\e[35m \W \$ \e[0m'


