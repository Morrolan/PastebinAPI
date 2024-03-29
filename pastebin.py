#!/usr/bin/env python

#############################################################################
#    Pastebin.py - Python 3.7 Pastebin API.
#    Copyright (C) 2012 - 2019 Ian Havelock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

# This software is a derivative work of:
# http://winappdbg.sourceforge.net/blog/pastebin.py

#############################################################################


__all__ = ['delete_paste', 'user_details', 'trending', 'pastes_by_user',
           'generate_user_key', 'paste', 'PastebinAPI', 'PastebinError']

import sys
import urllib
import requests


def convert_xml_to_json(xml_input):
    """

    :param xml_input:
    :return:
    """
    from xml.etree.ElementTree import fromstring
    import xmltodict
    import json

    # bf.data(fromstring(response.text))
    my_dict = xmltodict.parse("<pastes>{0}</pastes>".format(xml_input))

    paste_list = my_dict['pastes']['paste']

    new_pastes_list = []

    for paste in paste_list:
        new_pastes_list.append(dict(paste))

    new_pastes_dict = {
        "pastes": new_pastes_list
    }

    return json.dumps(new_pastes_dict)


class PastebinError(RuntimeError):
    """Pastebin API error.

    The error message returned by the web application is stored as the Python 
    exception message."""


class PastebinAPI(object):
    """Pastebin API interaction object.
  
    Public functions:
    
    paste -- Pastes a user-specified file or string using the new API-key POST 
    method.

    generate_user_key -- Generates a session-key that is required for other 
    functions.
    
    pastes_by_user -- Returns all public pastes submitted by the specified login
    credentials.
    
    trending -- Returns the top trending paste.
    
    user_details -- Returns details about the user for the specified API user 
    key.
    
    delete_paste -- Adds two numbers together and returns the result."""

    # String to determine bad API requests
    bad_request = 'Bad API request'

    # Base domain name
    base_domain = 'pastebin.com'

    # Valid Pastebin URLs begin with this string
    prefix_url = 'https://{0}'.format(base_domain)

    # Valid Pastebin URLs with a custom subdomain begin with this string
    subdomain_url = 'https://%%s.{0}/'.format(base_domain)

    # URL to the POST API
    api_url = 'https://{0}/api/api_post.php'.format(base_domain)

    # URL to the Login API
    api_login_url = 'https://{0}/api/api_login.php'.format(base_domain)

    # Valid paste_expire_date values (Never, 10 minutes, 1 Hour, 1 Day, 1 Month)
    paste_expire_date = ('N', '10M', '1H', '1D', '1M')

    # Valid paste_expire_date values (0 = public, 1 = unlisted, 2 = private)
    paste_private = ('public', 'unlisted', 'private')

    # Valid parse_format values
    paste_format = (
        '﻿4cs',  # 4CS
        '6502acme',  # 6502 ACME Cross Asse...
        '6502kickass',  # 6502 Kick Assembler
        '6502tasm',  # 6502 TASM/64TASS
        'abap',  # ABAP
        'actionscript',  # ActionScript
        'actionscript3',  # ActionScript 3
        'ada',  # Ada
        'aimms',  # AIMMS
        'algol68',  # ALGOL 68
        'apache',  # Apache Log
        'applescript',  # AppleScript
        'apt_sources',  # APT Sources
        'arduino',  # Arduino
        'arm',  # ARM
        'asm',  # ASM (NASM)
        'asp',  # ASP
        'asymptote',  # Asymptote
        'autoconf',  # autoconf
        'autohotkey',  # Autohotkey
        'autoit',  # AutoIt
        'avisynth',  # Avisynth
        'awk',  # Awk
        'bascomavr',  # BASCOM AVR
        'bash',  # Bash
        'basic4gl',  # Basic4GL
        'dos',  # Batch
        'bibtex',  # BibTeX
        'blitzbasic',  # Blitz Basic
        'b3d',  # Blitz3D
        'bmx',  # BlitzMax
        'bnf',  # BNF
        'boo',  # BOO
        'bf',  # BrainFuck
        'c',  # C
        'c_winapi',  # C (WinAPI)
        'c_mac',  # C for Macs
        'cil',  # C Intermediate Language
        'csharp',  # C#
        'cpp',  # C++
        'cpp-winapi',  # C++ (WinAPI)
        'cpp-qt',  # C++ (with Qt extensi...
        'c_loadrunner',  # C: Loadrunner
        'caddcl',  # CAD DCL
        'cadlisp',  # CAD Lisp
        'ceylon',  # Ceylon
        'cfdg',  # CFDG
        'chaiscript',  # ChaiScript
        'chapel',  # Chapel
        'clojure',  # Clojure
        'klonec',  # Clone C
        'klonecpp',  # Clone C++
        'cmake',  # CMake
        'cobol',  # COBOL
        'coffeescript',  # CoffeeScript
        'cfm',  # ColdFusion
        'css',  # CSS
        'cuesheet',  # Cuesheet
        'd',  # D
        'dart',  # Dart
        'dcl',  # DCL
        'dcpu16',  # DCPU-16
        'dcs',  # DCS
        'delphi',  # Delphi
        'oxygene',  # Delphi Prism (Oxygene)
        'diff',  # Diff
        'div',  # DIV
        'dot',  # DOT
        'e',  # E
        'ezt',  # Easytrieve
        'ecmascript',  # ECMAScript
        'eiffel',  # Eiffel
        'email',  # Email
        'epc',  # EPC
        'erlang',  # Erlang
        'euphoria',  # Euphoria
        'fsharp',  # F#
        'falcon',  # Falcon
        'filemaker',  # Filemaker
        'fo',  # FO Language
        'f1',  # Formula One
        'fortran',  # Fortran
        'freebasic',  # FreeBasic
        'freeswitch',  # FreeSWITCH
        'gambas',  # GAMBAS
        'gml',  # Game Maker
        'gdb',  # GDB
        'genero',  # Genero
        'genie',  # Genie
        'gettext',  # GetText
        'go',  # Go
        'groovy',  # Groovy
        'gwbasic',  # GwBasic
        'haskell',  # Haskell
        'haxe',  # Haxe
        'hicest',  # HicEst
        'hq9plus',  # HQ9 Plus
        'html4strict',  # HTML
        'html5',  # HTML 5
        'icon',  # Icon
        'idl',  # IDL
        'ini',  # INI file
        'inno',  # Inno Script
        'intercal',  # INTERCAL
        'io',  # IO
        'ispfpanel',  # ISPF Panel Definition
        'j',  # J
        'java',  # Java
        'java5',  # Java 5
        'javascript',  # JavaScript
        'jcl',  # JCL
        'jquery',  # jQuery
        'json',  # JSON
        'julia',  # Julia
        'kixtart',  # KiXtart
        'kotlin',  # Kotlin
        'latex',  # Latex
        'ldif',  # LDIF
        'lb',  # Liberty BASIC
        'lsl2',  # Linden Scripting
        'lisp',  # Lisp
        'llvm',  # LLVM
        'locobasic',  # Loco Basic
        'logtalk',  # Logtalk
        'lolcode',  # LOL Code
        'lotusformulas',  # Lotus Formulas
        'lotusscript',  # Lotus Script
        'lscript',  # LScript
        'lua',  # Lua
        'm68k',  # M68000 Assembler
        'magiksf',  # MagikSF
        'make',  # Make
        'mapbasic',  # MapBasic
        'markdown',  # Markdown
        'matlab',  # MatLab
        'mirc',  # mIRC
        'mmix',  # MIX Assembler
        'modula2',  # Modula 2
        'modula3',  # Modula 3
        '68000devpac',  # Motorola 68000 HiSof...
        'mpasm',  # MPASM
        'mxml',  # MXML
        'mysql',  # MySQL
        'nagios',  # Nagios
        'netrexx',  # NetRexx
        'newlisp',  # newLISP
        'nginx',  # Nginx
        'nim',  # Nim
        'text',  # None
        'nsis',  # NullSoft Installer
        'oberon2',  # Oberon 2
        'objeck',  # Objeck Programming L...
        'objc',  # Objective C
        'ocaml',  # OCaml
        'ocaml-brief',  # OCaml Brief
        'octave',  # Octave
        'oorexx',  # Open Object Rexx
        'pf',  # OpenBSD PACKET FILTER
        'glsl',  # OpenGL Shading
        'oobas',  # Openoffice BASIC
        'oracle11',  # Oracle 11
        'oracle8',  # Oracle 8
        'oz',  # Oz
        'parasail',  # ParaSail
        'parigp',  # PARI/GP
        'pascal',  # Pascal
        'pawn',  # Pawn
        'pcre',  # PCRE
        'per',  # Per
        'perl',  # Perl
        'perl6',  # Perl 6
        'php',  # PHP
        'php-brief',  # PHP Brief
        'pic16',  # Pic 16
        'pike',  # Pike
        'pixelbender',  # Pixel Bender
        'pli',  # PL/I
        'plsql',  # PL/SQL
        'postgresql',  # PostgreSQL
        'postscript',  # PostScript
        'povray',  # POV-Ray
        'powerbuilder',  # PowerBuilder
        'powershell',  # PowerShell
        'proftpd',  # ProFTPd
        'progress',  # Progress
        'prolog',  # Prolog
        'properties',  # Properties
        'providex',  # ProvideX
        'puppet',  # Puppet
        'purebasic',  # PureBasic
        'pycon',  # PyCon
        'python',  # Python
        'pys60',  # Python for S60
        'q',  # q/kdb+
        'qbasic',  # QBasic
        'qml',  # QML
        'rsplus',  # R
        'racket',  # Racket
        'rails',  # Rails
        'rbs',  # RBScript
        'rebol',  # REBOL
        'reg',  # REG
        'rexx',  # Rexx
        'robots',  # Robots
        'rpmspec',  # RPM Spec
        'ruby',  # Ruby
        'gnuplot',  # Ruby Gnuplot
        'rust',  # Rust
        'sas',  # SAS
        'scala',  # Scala
        'scheme',  # Scheme
        'scilab',  # Scilab
        'scl',  # SCL
        'sdlbasic',  # SdlBasic
        'smalltalk',  # Smalltalk
        'smarty',  # Smarty
        'spark',  # SPARK
        'sparql',  # SPARQL
        'sqf',  # SQF
        'sql',  # SQL
        'standardml',  # StandardML
        'stonescript',  # StoneScript
        'sclang',  # SuperCollider
        'swift',  # Swift
        'systemverilog',  # SystemVerilog
        'tsql',  # T-SQL
        'tcl',  # TCL
        'teraterm',  # Tera Term
        'thinbasic',  # thinBasic
        'typoscript',  # TypoScript
        'unicon',  # Unicon
        'uscript',  # UnrealScript
        'upc',  # UPC
        'urbi',  # Urbi
        'vala',  # Vala
        'vbnet',  # VB.NET
        'vbscript',  # VBScript
        'vedit',  # Vedit
        'verilog',  # VeriLog
        'vhdl',  # VHDL
        'vim',  # VIM
        'visualprolog',  # Visual Pro Log
        'vb',  # VisualBasic
        'visualfoxpro',  # VisualFoxPro
        'whitespace',  # WhiteSpace
        'whois',  # WHOIS
        'winbatch',  # Winbatch
        'xbasic',  # XBasic
        'xml',  # XML
        'xorg_conf',  # Xorg Config
        'xpp',  # XPP
        'yaml',  # YAML
        'z80',  # Z80 Assembler
        'zxbasic',  # ZXBasic
    )

    def __init__(self):
        pass

    def delete_paste(self, api_dev_key, api_user_key, api_paste_key):
        """Delete the paste specified by the api_paste_key.          
          
          
        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> paste_to_delete = pb.delete_paste('453a994e0e2f1efae07f8759e59e075b',
            ...                                 'c57a18e6c0ae228cd4bd16fe36da381a',
            ...                                 'WkgcTFtv')
            >>> print(paste_to_delete)
            Paste Removed     
            

        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.
        
        @type   api_user_key: string
        @param  api_user_key: The API User Key of a U{https://pastebin.com} registered user.
        
        @type   api_paste_key: string
        @param  api_paste_key: The Paste Key of the paste to be deleted (string after final / in U{https://pastebin.com} URL).

        @rtype: string
        @returns: A successful deletion returns 'Paste Removed'.
        """

        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Requires pre-registered account
        if api_user_key is not None:
            payload['api_user_key'] = str(api_user_key)

        # Key of the paste to be deleted.
        if api_paste_key is not None:
            payload['api_paste_key'] = str(api_paste_key)

        # Valid API option - 'user_details' in this instance
        payload['api_option'] = str('delete')

        # lets try to read the URL that we've just built.
        request_string = urllib.request.urlopen(self.api_url, urllib.parse.urlencode(payload))
        response = request_string.read()

        return response

    def user_details(self, api_dev_key, api_user_key):
        """Return user details of the user specified by the api_user_key.
        
        
        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> details = pb.user_details('453a994e0e2f1efae07f8759e59e075b',
            ...                         'c57a18e6c0ae228cd4bd16fe36da381a')
            >>> print(details)
            <user>
            <user_name>MonkeyPuzzle</user_name>
            <user_format_short>python</user_format_short>
            <user_expiration>N</user_expiration>
            <user_avatar_url>https://pastebin.com/i/guest.gif</user_avatar_url>
            <user_private>0</user_private>
            <user_website></user_website>
            <user_email>user@email.com</user_email>
            <user_location></user_location>
            <user_account_type>0</user_account_type>
            </user>
        
        
        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.
        
        @type   api_user_key: string
        @param  api_user_key: The API User Key of a U{https://pastebin.com} registered user.

        @rtype: string
        @returns: Returns an XML string containing user information.
        """

        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Requires pre-registered account to generate an api_user_key 
        # (see generate_user_key)
        if api_user_key is not None:
            payload['api_user_key'] = str(api_user_key)

        # Valid API option - 'user_details' in this instance
        payload['api_option'] = str('userdetails')

        # lets try to read the URL that we've just built.
        request_string = urllib.request.urlopen(self.api_url, urllib.parse.urlencode(payload))
        response = request_string.read()

        # do some basic error checking here so we can gracefully handle any 
        # errors we are likely to encounter
        if response.startswith(self.bad_request):
            raise PastebinError(response)

        elif not response.startswith('<user>'):
            raise PastebinError(response)

        return response

    def trending(self, api_dev_key):
        """Returns the top trending paste details.
        

        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> trending_pastes = pb.trending('453a994e0e2f1efae07f8759e59e075b')
            >>> print(trending_pastes)
            <paste>
            <paste_key>jjMRFDH6</paste_key>
            <paste_date>1333230838</paste_date>
            <paste_title></paste_title>
            <paste_size>6416</paste_size>
            <paste_expire_date>0</paste_expire_date>
            <paste_private>0</paste_private>
            <paste_format_long>None</paste_format_long>
            <paste_format_short>text</paste_format_short>
            <paste_url>https://pastebin.com/jjMRFDH6</paste_url>
            <paste_hits>6384</paste_hits>
            </paste>
            
        Note: Returns multiple trending pastes, not just 1.
        
        
        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.
        
        
        @rtype:  string
        @return: Returns the string (XML formatted) containing the top trending pastes.
        """

        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Valid API option - 'trends' is returns trending pastes
        payload['api_option'] = str('trends')

        # lets try to read the URL that we've just built.
        request_string = urllib.request.urlopen(self.api_url, urllib.parse.urlencode(payload))
        response = request_string.read()

        # do some basic error checking here so we can gracefully handle any 
        # errors we are likely to encounter
        if response.startswith(self.bad_request):
            raise PastebinError(response)

        elif not response.startswith('<paste>'):
            raise PastebinError(response)

        return response

    def pastes_by_user(self, api_dev_key, api_user_key, results_limit=None, format='XML'):
        """Returns all pastes for the provided api_user_key.
       
        
        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> details = pb.user_details('453a994e0e2f1efae07f8759e59e075b',
            ...                         'c57a18e6c0ae228cd4bd16fe36da381a',
            ...                         100)
            >>> print(details)
            <paste>
            <paste_key>DLiSspYT</paste_key>
            <paste_date>1332714730</paste_date>
            <paste_title>Pastebin.py - Python 3.2 Pastebin.com API</paste_title>
            <paste_size>25300</paste_size>
            <paste_expire_date>0</paste_expire_date>
            <paste_private>0</paste_private>
            <paste_format_long>Python</paste_format_long>
            <paste_format_short>python</paste_format_short>
            <paste_url>https://pastebin.com/DLiSspYT</paste_url>
            <paste_hits>70</paste_hits>
            </paste>
            
        Note: Returns multiple pastes, not just 1.
        
        
        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.
        
        @type   api_user_key: string
        @param  api_user_key: The API User Key of a U{https://pastebin.com} registered user.
        
        @type   results_limit: number
        @param  results_limit: The number of pastes to return between 1 - 1000.

        @rtype: string
        @returns: Returns an XML string containing number of specified pastes by user.
        """

        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Requires pre-registered account
        if api_user_key is not None:
            payload['api_user_key'] = str(api_user_key)

        # Number of results to return - between 1 & 1000, default = 50
        if results_limit is None:
            payload['api_results_limit'] = 50

        if results_limit is not None:
            if results_limit < 1:
                payload['api_results_limit'] = 50
            elif results_limit > 1000:
                payload['api_results_limit'] = 1000
            else:
                payload['api_results_limit'] = int(results_limit)

        # Valid API option - 'paste' is default for new paste
        payload['api_option'] = str('list')

        # lets try to read the URL that we've just built.
        response = requests.post(self.api_url, data=payload)

        # do some basic error checking here so we can gracefully handle any 
        # errors we are likely to encounter
        if response.text.startswith(self.bad_request):
            raise PastebinError(response.text)

        elif not response.text.startswith('<paste>'):
            raise PastebinError(response.text)

        if format in ['xml', 'XML']:
            return response.text

        elif format in ['json', 'JSON']:
            response = convert_xml_to_json(response.text)
            return response
        else:
            return response.text

    def generate_user_key(self, api_dev_key, username, password):
        """Generate a user session key - needed for other functions.
          
          
        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> my_key = pb.generate_user_key('453a994e0e2f1efae07f8759e59e075b',
            ...                             'MonkeyPuzzle',
            ...                             '12345678')
            >>> print(my_key)
            c57a18e6c0ae228cd4bd16fe36da381a
            
            
        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.
        
        @type   username: string
        @param  username: The username of a registered U{https://pastebin.com} account.
        
        @type   password: string
        @param  password: The password of a registered U{https://pastebin.com} account.

        @rtype: string
        @returns: Session key (api_user_key) to allow authenticated interaction to the API.
            
        """
        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Requires pre-registered pastebin account
        if username is not None:
            payload['api_user_name'] = str(username)

        # Requires pre-registered pastebin account
        if password is not None:
            payload['api_user_password'] = str(password)

        # lets try to read the URL that we've just built.
        response = requests.post(self.api_login_url, data=payload)

        # do some basic error checking here so we can gracefully handle any errors we are likely to encounter
        if response.text.startswith(self.bad_request):
            raise PastebinError(response.text)
        else:
            return response.text

    def paste(self, api_dev_key, api_paste_code,
              api_user_key=None, paste_name=None, paste_format=None,
              paste_private=None, paste_expire_date=None):
        """Submit a code snippet to Pastebin using the new API.


        Usage Example::
            >>> from pastebin import PastebinAPI
            >>> pb = PastebinAPI()
            >>> url = pb.paste('453a994e0e2f1efae07f8759e59e075b' ,
            ...               'Snippet of code to paste goes here',
            ...               paste_name = 'title of paste',
            ...               api_user_key = 'c57a18e6c0ae228cd4bd16fe36da381a',
            ...               paste_format = 'python',
            ...               paste_private = 'unlisted',
            ...               paste_expire_date = '10M')
            >>> print(url)
            https://pastebin.com/tawPUgqY


        @type   api_dev_key: string
        @param  api_dev_key: The API Developer Key of a registered U{https://pastebin.com} account.

        @type   api_paste_code: string
        @param  api_paste_code: The file or string to paste to body of the U{https://pastebin.com} paste.

        @type   api_user_key: string
        @param  api_user_key: The API User Key of a U{https://pastebin.com} registered user.
            If none specified, paste is made as a guest.

        @type   paste_name: string
        @param  paste_name: (Optional) Title of the paste.
            Default is to paste anonymously.

        @type  paste_format: string
        @param paste_format: (Optional) Programming language of the code being
            pasted. This enables syntax highlighting when reading the code in
            U{https://pastebin.com}. Default is no syntax highlighting (text is
            just text and not source code).

        @type  paste_private: string
        @param paste_private: (Optional) C{'public'} if the paste is public (visible
            by everyone), C{'unlisted'} if it's public but not searchable.
            C{'private'} if the paste is private and not searchable or indexed.
            The Pastebin FAQ (U{https://pastebin.com/faq}) claims
            private pastes are not indexed by search engines (aka Google).

        @type  paste_expire_date: str
        @param paste_expire_date: (Optional) Expiration date for the paste.
            Once past this date the paste is deleted automatically. Valid
            values are found in the L{PastebinAPI.paste_expire_date} class member.
            If not provided, the paste never expires.

        @rtype:  string
        @return: Returns the URL to the newly created paste.
        :param api_dev_key:
        :param api_paste_code:
        :param api_user_key:
        :param paste_name:
        :param paste_format:
        :param paste_private:
        :param paste_expire_date:
        :return:
        :param self:
        """

        # Valid api developer key
        payload = {'api_dev_key': str(api_dev_key)}

        # Code snippet to submit
        if api_paste_code is not None:
            payload['api_paste_code'] = str(api_paste_code)

        # Valid API option - 'paste' is default for new paste
        payload['api_option'] = str('paste')

        # API User Key
        if api_user_key is not None:
            payload['api_user_key'] = str(api_user_key)
        elif api_user_key is None:
            payload['api_user_key'] = str('')

        # Name of the poster
        if paste_name is not None:
            payload['api_paste_name'] = str(paste_name)

        # Syntax highlighting
        if paste_format is not None:
            paste_format = str(paste_format).strip().lower()
            payload['api_paste_format'] = paste_format

        # Is the snippet private?
        if paste_private is not None:
            if paste_private == 'public':
                payload['api_paste_private'] = int(0)
            elif paste_private == 'unlisted':
                payload['api_paste_private'] = int(1)
            elif paste_private == 'private':
                payload['api_paste_private'] = int(2)

        # Expiration for the snippet
        if paste_expire_date is not None:
            paste_expire_date = str(paste_expire_date).strip().upper()
            payload['api_paste_expire_date'] = paste_expire_date

        # lets try to read the URL that we've just built.
        response = requests.post(self.api_url, data=payload)

        # do some basic error checking here so we can gracefully handle any
        # errors we are likely to encounter
        if response.text.startswith(self.bad_request):
            raise PastebinError(response)
        elif not response.text.startswith(self.prefix_url):
            raise PastebinError(response)

        return response.text

######################################################

# api = PastebinAPI()
# delete_paste = api.delete_paste
# user_details = api.user_details
# trending = api.trending
# pastes_by_user = api.pastes_by_user
# generate_user_key = api.generate_user_key
# paste = api.paste

######################################################
