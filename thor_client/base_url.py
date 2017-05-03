"""The url that should be used in contact the Thor server. When Thor is deployed
locally, it make sense to use the localhost designation. On the other hand, when
deployed remotely, a particular URL needs to be provided.

Examples:
    To use a localhost server:

    >>> base_url = "http://127.0.0.1:5000/api/{}/"

    To use a designated computer accessible at a given domain and port:

    >>> base_url = "http://yourserver.com:PORT/api/{}/"
"""
base_url = "http://127.0.0.1:5000/api/{}/"
# base_url = "http://aa-lnx01.mitre.org:5000/api/{}/"
