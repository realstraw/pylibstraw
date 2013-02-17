import urllib2

def get_internet_files(urls, target_location):
    for url in urls:
        pdf_file = urllib2.urlopen(url)

        fname = url.split('/')[-1]
        fname = "{}/{}".format(target_location, fname)
        f = open(fname, 'w')
        f.write(pdf_file.read())
        f.close()
