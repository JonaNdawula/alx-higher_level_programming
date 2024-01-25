#!/bin/bash
#Takes in URL, sends request, and diasplays size
curl -sw '%{size_download}\n' -o /dev/null "$1"
