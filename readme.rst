============
Pastebin API
============
About
-----

The package allows you to communicate directly with Pastebin.com from your Python application, either logged in or anonymously. This can be handy 

for a number of reasons - dumping error logs before an abort, regular web based status updates, but can't be bothered getting a web-server running etc.

It allows you to do everything the API allows, which is:

- Paste, either logged in or anonymously
- 200+ selectable languages for syntax highlighting
- Set expiry times on pastes
- Set public/private/unlisted status for pastes
- See trending pastes
- See pastes by a particular user
- Delete your pastes
- Retrieve your user details
- Generate a session (user) key for added security
- Paste using the old, non-token anonymous API (for as long as they keep it open)




Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline: 

::
   
   $ python setup.py install


If you can use and install Python Egg's, you can do:

::

   $ easy_install Pastebin


And it will download the latest version from the Python Package Index.




Usage Examples
--------------

**Generate a user/session key** (this is required by other functions):

::

   >>> from pastebin import PastebinAPI
   >>> my_key = PastebinAPI.generate_user_key(api_dev_key, username, password)
   >>> print my_key



Return an XML list of **User Details** of user specified by API key.

::

   >>> details = PastebinAPI.user_details(api_dev_key, api_user_key)
   >>> print details



Return a list of **trending pastes**.  The result is in XML:

::

   >>> trending_pastes = PastebinAPI.trending(api_dev_key)
   >>> print trending_pastes



Return an XML list of all **pastes by user**.  Result limit defaults to none, so it will return all pastes:

::

   >>> details = x.user_details(api_dev_key, api_user_key, results_limit = None)



**Delete a paste**:

::

   >>> PastebinAPI.delete_paste(api_dev_key, api_user_key, api_paste_key)


**Paste** to Pastebin, where api_paste_code is the contents of your paste.  This will accept any valid Python data type:

::

   >>> PastebinAPI.paste(api_dev_key, api_paste_code, api_user_key = None, paste_name = None, 
   ...                   paste_format = None, paste_private = None, 
   ...                   paste_expire_date = None)



Note that any parameter which is listed about as ' = *None*' is optional. 
Details of valid input parameters for paste function are below.


Valid paste_private values: 

- 'public'
- 'unlisted'
- 'private'



Valid paste_expire_date values:

======  ===========
Input   Description
======  ===========
'N'     Never
'10M'   10 minutes
'1H'    1 hour
'1D'    1 day
'1M'    1 month
======  ===========


Valid parse_format values:


================  =============================== 
     Input                   Language
================  =============================== 
'4cs'             4CS
'6502acme'        6502 ACME Cross Assembler
'6502kickass'     6502 Kick Assembler
'6502tasm'        6502 TASM/64TASS
'abap'            ABAP
'actionscript'    ActionScript
'actionscript3'   ActionScript 3
'ada'             Ada
'algol68'         ALGOL 68
'apache'          Apache Log
'applescript'     AppleScript
'apt_sources'     APT Sources
'asm'             ASM (NASM)
'asp'             ASP
'autoconf'        autoconf
'autohotkey'      Autohotkey
'autoit'          AutoIt
'avisynth'        Avisynth
'awk'             Awk
'bascomavr'       BASCOM AVR
'bash'            Bash
'basic4gl'        Basic4GL
'bibtex'          BibTeX
'blitzbasic'      Blitz Basic
'bnf'             BNF
'boo'             BOO
'bf'              BrainFuck
'c'               C
'c_mac'           C for Macs
'cil'             C Intermediate Language
'csharp'          C#
'cpp'             C++
'cpp-qt'          C++ (with QT extensions)
'c_loadrunner'    C: Loadrunner
'caddcl'          CAD DCL
'cadlisp'         CAD Lisp
'cfdg'            CFDG
'chaiscript'      ChaiScript
'clojure'         Clojure
'klonec'          Clone C
'klonecpp'        Clone C++
'cmake'           CMake
'cobol'           COBOL
'coffeescript'    CoffeeScript
'cfm'             ColdFusion
'css'             CSS
'cuesheet'        Cuesheet
'd'               D
'dcs'             DCS
'delphi'          Delphi
'oxygene'         Delphi Prism (Oxygene)
'diff'            Diff
'div'             DIV
'dos'             DOS
'dot'             DOT
'e'               E
'ecmascript'      ECMAScript
'eiffel'          Eiffel
'email'           Email
'epc'             EPC
'erlang'          Erlang
'fsharp'          F#
'falcon'          Falcon
'fo'              FO Language
'f1'              Formula One
'fortran'         Fortran
'freebasic'       FreeBasic
'freeswitch'      FreeSWITCH
'gambas'          GAMBAS
'gml'             Game Maker
'gdb'             GDB
'genero'          Genero
'genie'           Genie
'gettext'         GetText
'go'              Go
'groovy'          Groovy
'gwbasic'         GwBasic
'haskell'         Haskell
'hicest'          HicEst
'hq9plus'         HQ9 Plus
'html4strict'     HTML
'html5'           HTML 5
'icon'            Icon
'idl'             IDL
'ini'             INI file
'inno'            Inno Script
'intercal'        INTERCAL
'io'              IO
'j'               J
'java'            Java
'java5'           Java 5
'javascript'      JavaScript
'jquery'          jQuery
'kixtart'         KiXtart
'latex'           Latex
'lb'              Liberty BASIC
'lsl2'            Linden Scripting
'lisp'            Lisp
'llvm'            LLVM
'locobasic'       Loco Basic
'logtalk'         Logtalk
'lolcode'         LOL Code
'lotusformulas'   Lotus Formulas
'lotusscript'     Lotus Script
'lscript'         LScript
'lua'             Lua
'm68k'            M68000 Assembler
'magiksf'         MagikSF
'make'            Make
'mapbasic'        MapBasic
'matlab'          MatLab
'mirc'            mIRC
'mmix'            MIX Assembler
'modula2'         Modula 2
'modula3'         Modula 3
'68000devpac'     Motorola 68000 HiSoft Dev
'mpasm'           MPASM
'mxml'            MXML
'mysql'           MySQL
'newlisp'         newLISP
'text'            None
'nsis'            NullSoft Installer
'oberon2'         Oberon 2
'objeck'          Objeck Programming Langua
'objc'            Objective C
'ocaml-brief'     OCalm Brief
'ocaml'           OCaml
'pf'              OpenBSD PACKET FILTER
'glsl'            OpenGL Shading
'oobas'           Openoffice BASIC
'oracle11'        Oracle 11
'oracle8'         Oracle 8
'oz'              Oz
'pascal'          Pascal
'pawn'            PAWN
'pcre'            PCRE
'per'             Per
'perl'            Perl
'perl6'           Perl 6
'php'             PHP
'php-brief'       PHP Brief
'pic16'           Pic 16
'pike'            Pike
'pixelbender'     Pixel Bender
'plsql'           PL/SQL
'postgresql'      PostgreSQL
'povray'          POV-Ray
'powershell'      Power Shell
'powerbuilder'    PowerBuilder
'proftpd'         ProFTPd
'progress'        Progress
'prolog'          Prolog
'properties'      Properties
'providex'        ProvideX
'purebasic'       PureBasic
'pycon'           PyCon
'python'          Python
'q'               q/kdb+
'qbasic'          QBasic
'rsplus'          R
'rails'           Rails
'rebol'           REBOL
'reg'             REG
'robots'          Robots
'rpmspec'         RPM Spec
'ruby'            Ruby
'gnuplot'         Ruby Gnuplot
'sas'             SAS
'scala'           Scala
'scheme'          Scheme
'scilab'          Scilab
'sdlbasic'        SdlBasic
'smalltalk'       Smalltalk
'smarty'          Smarty
'sql'             SQL
'systemverilog'   SystemVerilog
'tsql'            T-SQL
'tcl'             TCL
'teraterm'        Tera Term
'thinbasic'       thinBasic
'typoscript'      TypoScript
'unicon'          Unicon
'uscript'         UnrealScript
'vala'            Vala
'vbnet'           VB.NET
'verilog'         VeriLog
'vhdl'            VHDL
'vim'             VIM
'visualprolog'    Visual Pro Log
'vb'              VisualBasic
'visualfoxpro'    VisualFoxPro
'whitespace'      WhiteSpace
'whois'           WHOIS
'winbatch'        Winbatch
'xbasic'          XBasic
'xml'             XML
'xorg_conf'       Xorg Config
'xpp'             XPP
'yaml'            YAML
'z80'             Z80 Assembler
'zxbasic'         ZXBasic
================  ===============================