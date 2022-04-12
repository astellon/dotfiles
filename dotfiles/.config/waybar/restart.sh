#!/bin/sh

killall -SIGKILL waybar
waybar &> $HOME/.config/waybar/waybar.log &