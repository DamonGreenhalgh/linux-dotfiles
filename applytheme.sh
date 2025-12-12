#!/bin/sh

# Author: Damon Greenhalgh
# Date: 30/10/2025
# Description: This script applies the theme to configs to apps

configPath=/home/damon/.config    # The path to your app configs, usually ~/.config/*
currentPath=/home/damon/Documents/rice

# Copy over and replace files
cp -r $currentPath/waybar/. $configPath/waybar/
cp -r $currentPath/eww/. $configPath/eww/
cp -r $currentPath/fastfetch/. $configPath/fastfetch/
cp -r $currentPath/hypr/. $configPath/hypr/
cp -r $currentPath/kitty/. $configPath/kitty/
cp -r $currentPath/mako/. $configPath/mako/
cp -r $currentPath/Code/. $configPath/Code/
cp -r $currentPath/wofi/. $configPath/wofi/
cp -r $currentPath/firefox/. /home/damon/.mozilla/firefox/u0oe936c.default-release
cp $currentPath/bashrc /home/damon/.bashrc

# reload apps with new configs
hyprctl reload
pkill hyprpaper
hyprpaper &
pkill waybar
waybar &
pkill mako

sleep 0.5
clear
fastfetch
