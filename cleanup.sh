#!/bin/sh

# Script to clear out stale files
sudo paccache -rk1
sudo pacman -Rns $(pacman -Qdtq)
sudo journalctl --vacuum-time=2weeks
rm -rf ~/.cache/*
rm -rf ~/Documents/Logs/*