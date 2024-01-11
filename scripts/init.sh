#!/bin/bash

# Run this script once before running main.py program
# This script inits the data from external sources (web APIs) to get the necessary data for creating pandas Data Frame.

# create virtual environment and install pip packages
# VENV_DIR="virtualenv"
# source $VENV_DIR/bin/activate
# pip install dotenv 


cpu_threads_total=$(nproc --all)

echo "There are $cpu_threads_total threads available on Your machine. Please select the amount You'd like to use for getting web API data:"
read cpu_threads_amount

if(($cpu_threads_amount >= $cpu_threads_total ||  $cpu_threads_amount < 1))
then
  echo "❌ Can not reserve request amount of threads- selected more than maximum amount ($cpu_threads_total) or less than 1."
  exit 0
fi

python3 main.py $cpu_threads_amount || {
  echo "❌ Failed to load the data. Please try again"
  exit 1
}
echo "✅ Success." 
