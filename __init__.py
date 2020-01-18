import os
from os import listdir
from calibre.customize import FileTypePlugin


class HelloWorld(FileTypePlugin):

    name = 'Delete after conversion'  # Name of the plugin
    description = 'Deletes original file after conversions'
    # Platforms this plugin will run on
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'jmoore914'  # The author of this plugin
    version = (1, 0, 0)   # The version number of this plugin
    # The file types that this plugin will be applied to
    file_types = set(['epub', 'mobi', 'original_mobi'])
    on_postprocess = True  # Run this plugin after conversion is complete
    minimum_calibre_version = (0, 7, 53)

    def run(self, path_to_ebook):
        from calibre.ebooks.metadata.meta import get_metadata
        from calibre.library import db
        import time
        file = open(path_to_ebook, 'r+b')
        ext = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        db = db('C:/Users/jmoor/Docs/eBooks/Calibre').new_api
        title = mi.title
        author = mi.authors[0]
        ids = list(db.search('title:'+title + ' author:'+author))
        db.remove_formats({ids[0]: ['ORIGINAL_MOBI', 'epub', 'azw3']})
        searchResults = db.search('formats:"=ORIGINAL_MOBI"')
        for bookId in searchResults:
            try:
                db.remove_formats({bookId: ['original_mobi']})
            except:
                pass
