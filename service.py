from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import midcrawler
import wget
import re
from pathlib import Path, PureWindowsPath
import os

configure_logging()
runner = CrawlerRunner()


def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    '''import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    value = re.sub('[-\s]+', '-', value)
    return str(value)'''
    return str(PureWindowsPath(Path(value)))

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(midcrawler.GetArtistis)
    print("-----" + str(len(midcrawler.GetArtistis.links)))
    yield runner.crawl(midcrawler.GetMusics, urls=[x[1] for x in midcrawler.GetArtistis.links])
    print("-----" + str(len(midcrawler.GetMusics.links)))
    reactor.stop()

    for link in midcrawler.GetMusics.links:
        try:
            print(link[2])
            print(link[0])
            print(link[1])
            os.chdir('c:/temp/midi/')
            wget.download(link[2])#,slugify('c:/temp/midi/' + link[0] + link[1] + '.mid'))
        except:
            continue

crawl()
reactor.run() # the s