# Prerequisites
## Step 1: update the all packages, If necessary
```bash
apt update
apt upgrade
```
## Step 2: Download 'google-chrome' stable package
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
## Step 3: Install 'google-chrome'
```bash
apt-get install -y ./google-chrome-stable_current_amd64.deb
```
## Step 4: Check installed 'google-chrome' version
```bash
# google-chrome --version
Google Chrome 123.0.6312.86
```
## Step 5: Install selenium, webdriver-manager
```bash
pip3 install selenium
pip3 install webdriver-manager
```
# How To Use
```bash
python Automated_Bruteforce.py http://example.com.com/login /path/to/wordlist.txt
```
# Damo Working
