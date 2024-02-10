#!/bin/bash

PROJECT_NAME="palestine"
VENV_DIR="virtualenv"

echo "Creating virtual environment..."
sudo apt install python3-venv
python3 -m venv $VENV_DIR

source $VENV_DIR/bin/activate

echo "Installing packages..."
pip install aiohttp==3.9.1 \
             aiosignal==1.3.1 \
             annotated-types==0.6.0 \
             anyio==4.2.0 \
             async-timeout==4.0.3 \
             attrs==23.2.0 \
             certifi==2023.11.17 \
             charset-normalizer==3.3.2 \
             dataclasses-json==0.6.3 \
             distro==1.9.0 \
             exceptiongroup==1.2.0 \
             frozenlist==1.4.1 \
             greenlet==3.0.3 \
             h11==0.14.0 \
             httpcore==1.0.2 \
             httpx==0.26.0 \
             idna==3.6 \
             iniconfig==2.0.0 \
             joblib==1.3.2 \
             jsonpatch==1.33 \
             jsonpointer==2.4 \
             langsmith==0.0.77 \
             marshmallow==3.20.1 \
             multidict==6.0.4 \
             mypy-extensions==1.0.0 \
             numpy==1.26.2 \
             openai==1.6.1 \
             packaging==23.2 \
             pandas \
             pluggy==1.3.0 \
             pydantic==2.5.3 \
             pydantic_core==2.14.6 \
             pytest==7.4.4 \
             python-dateutil==2.8.2 \
             python-dotenv==1.0.0 \
             pytz==2023.3.post1 \
             PyYAML==6.0.1 \
             regex==2023.12.25 \
             requests==2.31.0 \
             scikit-learn==1.3.2 \
             scipy==1.11.4 \
             six==1.16.0 \
             sniffio==1.3.0 \
             SQLAlchemy==2.0.25 \
             tenacity==8.2.3 \
             threadpoolctl==3.2.0 \
             tiktoken==0.5.2 \
             tomli==2.0.1 \
             tqdm==4.66.1 \
             typing-inspect==0.9.0 \
             typing_extensions==4.9.0 \
             tzdata==2023.4 \
             urllib3==2.1.0 \
             yarl==1.9.4

echo "✅ Successfuly installed packages"


echo "Checking for data files about islamic and jewish holidays..."
ISLAMIC_HOLIDAYS="../data/islamic_holidays.csv"
JEWISH_HOLIDAYS="../data/jewish_holidays.csv"

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
    elif (( $cpu_threads_amount >= $cpu_threads_total ||  $cpu_threads_amount < 1 ))
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

echo "Now running main.py program..."
cd .. && python3 main.py