## NotifyMe

This is a modification of the example Python code from the [Notify Me](https://www.thomptronics.com/about/notify-me) Amazon Alexa skill. 

It accepts command line input and can read the API key from a text file, either in the script directory by default or, you can tell it the path using the --api-key-file argument.

Admittedly written with the help of ChatGPT. Just to see if I could do it.

## Installing

```bash
git clone https://github.com/BigFunnyGiant/python-notifyme # clone the repository
cd python-notifyme
cp whatismyip.sh /usr/local/bin
```
or copy it to somewhere you like, maybe in the PATH so you can execute it from anywhere


## Usage
./notify_me.py "Hello, World!"\
or\
./notify_me.py "Hello, World!" --api-key-file /path/to/api_key.txt


## Dependencies
- Python 3
