# load zplug
source ~/.zplug/init.zsh

# index plugins
zplug "zsh-users/zsh-history-substring-search"
zplug "zsh-users/zsh-syntax-highlighting"
zplug "zsh-users/zsh-autosuggestions"
zplug "zsh-users/zsh-completions"

# install plugins
if ! zplug check --verbose; then
  printf "Install? [y/N]: "
  if read -q; then
    echo; zplug install
  fi
fi

zplug load

autoload -Uz compinit && compinit
autoload -Uz colors && colors

#zstyles
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
zstyle ':completion:*:default' menu select=2

#starship prompt
eval "$(starship init zsh)"

# setopt
setopt autol_ist
setopt auto_cd
setopt auto_menu
setopt auto_pushd
setopt complete_in_word  
setopt nobeep 
setopt pushd_ignore_dups

# aliases
alias -g ...='../..'
alias -g ....='../../..'
alias -g .....='../../../..'

alias ls='ls --color'
alias la='ls -la'

alias gt='git'
alias gti='git'
alias gs='git status'
alias ga='git add .'
alias gdj='git diff --color-words=$'\''[^\x80-\xbf][\x80-\xbf]*'\'''

alias dr='docker run'
alias drr='docker run --rm'