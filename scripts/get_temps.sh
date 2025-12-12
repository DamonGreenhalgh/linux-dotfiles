#!/bin/bash

awk '{print int($1/1000)}' /sys/class/hwmon/hwmon1/temp1_input
