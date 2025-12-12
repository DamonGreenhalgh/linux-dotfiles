#!/bin/bash

nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | awk -F, '{printf "%sMiB /%sMiB\n", $1, $2}'
