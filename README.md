# Thor Python Client

This repository contains the Thor Python Client, which is a client-side interface for Thor Server. The Thor Server and Thor Python Client together provide a light-weight and powerful architecture for Bayesian optimization in Python.

## Installation

1. Install dependent libraries with pip. `pip install -r requirements.txt`
2. Clone this repository. `git clone git@github.com:JamesBrofos/Thor-Python-Client.git`
3. Run the `setup.py` function to install the client-side software: `python setup.py install`
4. Make sure you have signed up for an account with Thor.
5. If you are using Thor for multiple projects, you could place the `config.ini.example` configuration file in your home directory as `~/.thorconfig.ini`. The client will look first in the current directory, and then in your home directory.
6. Edit your new config file to include your `AUTH_TOKEN`, available from your Thor server account, and the `base_url` of your Thor server.  *Note*: leave the `/api/{}/` portion of the `base_url` configuration parameter unchanged; just update the protocol, hostname, and port, if necessary.
