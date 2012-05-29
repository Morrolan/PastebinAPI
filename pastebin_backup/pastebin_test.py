#!/usr/bin/env python

__all__ = ['paste', 'Pastebin', 'PastebinError']

import urllib

class PastebinError(RuntimeError):
      """
      here we simply return the error as a runtime error
      """

class Pastebin(object):
      
      # URL to the POST API    
      _api_url= 'http://pastebin.com/api/api_post.php'


      @classmethod
      def paste(cls, api_dev_key, paste_code):
        
        
        # Valid api developer key
        argv = {'api_dev_key' : str(api_dev_key) }
        
        # Code snippet to submit
        if paste_code is not None:
          argv['api_paste_code'] = str(paste_code)
        
        # lets try to read the URL that we've just built.
        request = urllib.urlopen(cls._api_url, urllib.urlencode(argv))
        response = submit_paste(request)
        return response



      def submit_paste(request_string):    
        
        response = request_string.read()
        # do some error checking here, but not relevant to the issue   
        return response
      
      
paste = Pastebin.paste
#submit_paste = Pastebin.submit_paste



if __name__ == "__main__":
    import sys