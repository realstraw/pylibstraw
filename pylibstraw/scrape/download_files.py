import urllib2


def get_internet_files(urls, target_location):
    successful_downloads = []
    failed_downloads = []
    for url in urls:
        print "getting file from url: {}".format(url)
        try:
            pdf_file = urllib2.urlopen(url)
            successful_downloads.append(url)
            fname = url.split('/')[-1]
            fname = "{}/{}".format(target_location, fname)
            with open(fname, 'w') as f:
                f.write(pdf_file.read())
        except urllib2.HTTPError:
            failed_downloads.append(url)

    # print out a summary
    print "Successfully downloaded:"
    print '\n'.join(successful_downloads)
    print "Failed downloaded:"
    print '\n'.join(failed_downloads)

    print "Summary: successful count is {}\nfailed count is "\
        "{}".format(len(successful_downloads), len(failed_downloads))
