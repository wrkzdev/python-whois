# Features #
  * Python wrapper for Linux "whois" command
  * simple interface to access parsed WHOIS data for a given domain
  * able to extract data for all the popular TLDs (com, org, net, pl, ...)
  * query a WHOIS server directly instead of going through an intermediate web service like many others do
  * no external dependencies
  * works with Python 2.4+ and Python 3.x
  * all dates as datetime objects
  * possibility to cache results


# Usage example #
```
>>> import whois
>>> domain = whois.query('google.com')

>>> print(domain.__dict__)
{'expiration_date': datetime.datetime(2020, 9, 14, 0, 0), 'last_updated': datetime.datetime(2011, 7, 20, 0, 0), 'registrar': 'MARKMONITOR INC.', 'name': 'google.com', 'creation_date': datetime.datetime(1997, 9, 15, 0, 0)}

>>> print(domain.name)
google.com

>>> print(domain.expiration_date)
2020-09-14 00:00:00
```


# TODO #
  * timeout


# Download #
```
$ sudo easy_install whois
```


# Related projects #
  * [pywhois](http://code.google.com/p/pywhois/) 0.1
  * [yawhois](http://code.google.com/p/yawhois/) 0.1

These projects solve this same problem, but do not have support for Python 3 or quality of their performance did not satisfy me. Perhaps it follows from this is the first versions of these libraries.