import whois

w = whois.query('daft.ie', ignore_returncode=1)
if w:
    wd = w.__dict__
    for k, v in wd.items():
        print('%20s\t"%s"' % (k, v))
