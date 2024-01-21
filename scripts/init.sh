#!/bin/bash

# Run this script once before running main.py program
# This script inits the data from external sources (web APIs) to get the necessary data for creating pandas Data Frame.

# create virtual environment and install pip packages
# VENV_DIR="virtualenv"
# source $VENV_DIR/bin/activate
# pip install dotenv 


ISLAMIC_HOLIDAYS="data/islamic_holidays.py"
JEWISH_HOLIDAYS="data/jewish_holidays.py"

cd scripts

if [ ! -f "$ISLAMIC_HOLIDAYS" ]
  then
    cpu_threads_total=$(nproc --all)
    echo "No data exists for islamic holidays. Getting the data is a time consuming task and can be sped up by working on several CPU threds."
    echo "If you are willing to provide more than 1 thread for this operation, please enter the number of threads (Your CPU has a total of $cpu_threads_total threads). If you don't want to increase CPU threads usage, please do not type anything and hit ENTER"

    read cpu_threads_amount

    if [ -z "$cpu_threads_amount" ]
      then
        cpu_threads_amount=1
      fi

    elif (($cpu_threads_amount >= $cpu_threads_total ||  $cpu_threads_amount < 1))
      then
        echo "❌ Can not reserve request amount of threads- selected more than maximum amount ($cpu_threads_total) or less than 1."
        exit 0
      fi

    python3 import_islamic_holidays.py $cpu_threads_amount || {
      echo "❌ Failed to load the data. Please try again"
      exit 1
    }
    echo "✅ Successfuly got islamic holidays data" 

  fi


if [ ! -f "$JEWISH_HOLIDAYS" ]
  then
    echo "No data exists for jewish holidays. The program will get the data in a moment."
    python3 import_jewish_holidays.py || {
      echo "❌ Failed to load the data. Please try again"
      exit 1
    }
    echo "✅ Successfuly got jewish holidays data" 

  fi


python3 main.py