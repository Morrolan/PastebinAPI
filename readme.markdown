
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

  
`$ python setup.py install`


If you can use and install Python Egg's, you can do:


`$ easy_install Pastebin`


And it will download the latest version from the Python Package Index.




Usage Examples
--------------

**Generate a user/session key** (this is required by other functions):

```python 
from pastebin import PastebinAPI
my_key = PastebinAPI.generate_user_key(api_dev_key, username, password)
print my_key
```


Return an XML list of **User Details** of user specified by API key.

```python 
details = PastebinAPI.user_details(api_dev_key, api_user_key)
print details
```


Return a list of **trending pastes**.  The result is in XML:

```python 
trending_pastes = PastebinAPI.trending(api_dev_key)
print trending_pastes
```


Return an XML list of all **pastes by user**.  Result limit defaults to none, so it will return all pastes:

```python 
details = x.user_details(api_dev_key, api_user_key, results_limit = None)
```


**Delete a paste**:

```python 
PastebinAPI.delete_paste(api_dev_key, api_user_key, api_paste_key)
```

**Paste** to Pastebin, where api_paste_code is the contents of your paste.  This will accept any valid Python data type:

```python 
PastebinAPI.paste(api_dev_key, api_paste_code, api_user_key = None, 
                   paste_name = None, paste_format = None, 
                   paste_private = None, paste_expire_date = None)
```



Note that any parameter which is listed about as ' = *None*' is optional. 
Details of valid input parameters for paste function are below.


Valid paste_private values: 

- 'public'
- 'unlisted'
- 'private'



Valid paste_expire_date values:


<table border="0">
<tr>
<th>Input</th><th>Description</th>
</tr>
<tr>
<td>'N'</td><td>Never</td>
</tr>
<tr>
<td>'10M'</td><td>10 minutes</td>
</tr>
<tr>
<td>'1H'</td><td>1 hour</td>
</tr>
<tr>
<td>'1D'</td><td>1 day</td>
</tr>
<tr>
<td>'1M'</td><td>1 month</td>
</tr>
</table> 
   
    



Valid parse_format values:


<table border="0">
<tr>
<th>Input</th>
<th>Language</th>
</tr>
<tr><td>'4cs'</td><td>4CS</td></tr>
<tr><td>'6502acme'</td><td>6502 ACME Cross Assembler</td></tr>
<tr><td>'6502kickass'</td><td>6502 Kick Assembler</td></tr>
<tr><td>'6502tasm'</td><td>6502 TASM/64TASS</td></tr>
<tr><td>'abap'</td><td>ABAP</td></tr>
<tr><td>'actionscript'</td><td>ActionScript</td></tr>
<tr><td>'actionscript3'</td><td>ActionScript 3</td></tr>
<tr><td>'ada'</td><td>Ada</td></tr>
<tr><td>'algol68'</td><td>ALGOL 68</td></tr>
<tr><td>'apache'</td><td>Apache Log</td></tr>
<tr><td>'applescript'</td><td>AppleScript</td></tr>
<tr><td>'apt_sources'</td><td>APT Sources</td></tr>
<tr><td>'asm'</td><td>ASM (NASM)</td></tr>
<tr><td>'asp'</td><td>ASP</td></tr>
<tr><td>'autoconf'</td><td>autoconf</td></tr>
<tr><td>'autohotkey'</td><td>Autohotkey</td></tr>
<tr><td>'autoit'</td><td>AutoIt</td></tr>
<tr><td>'avisynth'</td><td>Avisynth</td></tr>
<tr><td>'awk'</td><td>Awk</td></tr>
<tr><td>'bascomavr'</td><td>BASCOM AVR</td></tr>
<tr><td>'bash'</td><td>Bash</td></tr>
<tr><td>'basic4gl'</td><td>Basic4GL</td></tr>
<tr><td>'bibtex'</td><td>BibTeX</td></tr>
<tr><td>'blitzbasic'</td><td>Blitz Basic</td></tr>
<tr><td>'bnf'</td><td>BNF</td></tr>
<tr><td>'boo'</td><td>BOO</td></tr>
<tr><td>'bf'</td><td>BrainFuck</td></tr>
<tr><td>'c'</td><td>C</td></tr>
<tr><td>'c_mac'</td><td>C for Macs</td></tr>
<tr><td>'cil'</td><td>C Intermediate Language</td></tr>
<tr><td>'csharp'</td><td>C#</td></tr>
<tr><td>'cpp'</td><td>C++</td></tr>
<tr><td>'cpp-qt'</td><td>C++ (with QT extensions)</td></tr>
<tr><td>'c_loadrunner'</td><td>C: Loadrunner</td></tr>
<tr><td>'caddcl'</td><td>CAD DCL</td></tr>
<tr><td>'cadlisp'</td><td>CAD Lisp</td></tr>
<tr><td>'cfdg'</td><td>CFDG</td></tr>
<tr><td>'chaiscript'</td><td>ChaiScript</td></tr>
<tr><td>'clojure'</td><td>Clojure</td></tr>
<tr><td>'klonec'</td><td>Clone C</td></tr>
<tr><td>'klonecpp'</td><td>Clone C++</td></tr>
<tr><td>'cmake'</td><td>CMake</td></tr>
<tr><td>'cobol'</td><td>COBOL</td></tr>
<tr><td>'coffeescript'</td><td>CoffeeScript</td></tr>
<tr><td>'cfm'</td><td>ColdFusion</td></tr>
<tr><td>'css'</td><td>CSS</td></tr>
<tr><td>'cuesheet'</td><td>Cuesheet</td></tr>
<tr><td>'d'</td><td>D</td></tr>
<tr><td>'dcs'</td><td>DCS</td></tr>
<tr><td>'delphi'</td><td>Delphi</td></tr>
<tr><td>'oxygene'</td><td>Delphi Prism (Oxygene)</td></tr>
<tr><td>'diff'</td><td>Diff</td></tr>
<tr><td>'div'</td><td>DIV</td></tr>
<tr><td>'dos'</td><td>DOS</td></tr>
<tr><td>'dot'</td><td>DOT</td></tr>
<tr><td>'e'</td><td>E</td></tr>
<tr><td>'ecmascript'</td><td>ECMAScript</td></tr>
<tr><td>'eiffel'</td><td>Eiffel</td></tr>
<tr><td>'email'</td><td>Email</td></tr>
<tr><td>'epc'</td><td>EPC</td></tr>
<tr><td>'erlang'</td><td>Erlang</td></tr>
<tr><td>'fsharp'</td><td>F#</td></tr>
<tr><td>'falcon'</td><td>Falcon</td></tr>
<tr><td>'fo'</td><td>FO Language</td></tr>
<tr><td>'f1'</td><td>Formula One</td></tr>
<tr><td>'fortran'</td><td>Fortran</td></tr>
<tr><td>'freebasic'</td><td>FreeBasic</td></tr>
<tr><td>'freeswitch'</td><td>FreeSWITCH</td></tr>
<tr><td>'gambas'</td><td>GAMBAS</td></tr>
<tr><td>'gml'</td><td>Game Maker</td></tr>
<tr><td>'gdb'</td><td>GDB</td></tr>
<tr><td>'genero'</td><td>Genero</td></tr>
<tr><td>'genie'</td><td>Genie</td></tr>
<tr><td>'gettext'</td><td>GetText</td></tr>
<tr><td>'go'</td><td>Go</td></tr>
<tr><td>'groovy'</td><td>Groovy</td></tr>
<tr><td>'gwbasic'</td><td>GwBasic</td></tr>
<tr><td>'haskell'</td><td>Haskell</td></tr>
<tr><td>'hicest'</td><td>HicEst</td></tr>
<tr><td>'hq9plus'</td><td>HQ9 Plus</td></tr>
<tr><td>'html4strict'</td><td>HTML</td></tr>
<tr><td>'html5'</td><td>HTML 5</td></tr>
<tr><td>'icon'</td><td>Icon</td></tr>
<tr><td>'idl'</td><td>IDL</td></tr>
<tr><td>'ini'</td><td>INI file</td></tr>
<tr><td>'inno'</td><td>Inno Script</td></tr>
<tr><td>'intercal'</td><td>INTERCAL</td></tr>
<tr><td>'io'</td><td>IO</td></tr>
<tr><td>'j'</td><td>J</td></tr>
<tr><td>'java'</td><td>Java</td></tr>
<tr><td>'java5'</td><td>Java 5</td></tr>
<tr><td>'javascript'</td><td>JavaScript</td></tr>
<tr><td>'jquery'</td><td>jQuery</td></tr>
<tr><td>'kixtart'</td><td>KiXtart</td></tr>
<tr><td>'latex'</td><td>Latex</td></tr>
<tr><td>'lb'</td><td>Liberty BASIC</td></tr>
<tr><td>'lsl2'</td><td>Linden Scripting</td></tr>
<tr><td>'lisp'</td><td>Lisp</td></tr>
<tr><td>'llvm'</td><td>LLVM</td></tr>
<tr><td>'locobasic'</td><td>Loco Basic</td></tr>
<tr><td>'logtalk'</td><td>Logtalk</td></tr>
<tr><td>'lolcode'</td><td>LOL Code</td></tr>
<tr><td>'lotusformulas'</td><td>Lotus Formulas</td></tr>
<tr><td>'lotusscript'</td><td>Lotus Script</td></tr>
<tr><td>'lscript'</td><td>LScript</td></tr>
<tr><td>'lua'</td><td>Lua</td></tr>
<tr><td>'m68k'</td><td>M68000 Assembler</td></tr>
<tr><td>'magiksf'</td><td>MagikSF</td></tr>
<tr><td>'make'</td><td>Make</td></tr>
<tr><td>'mapbasic'</td><td>MapBasic</td></tr>
<tr><td>'matlab'</td><td>MatLab</td></tr>
<tr><td>'mirc'</td><td>mIRC</td></tr>
<tr><td>'mmix'</td><td>MIX Assembler</td></tr>
<tr><td>'modula2'</td><td>Modula 2</td></tr>
<tr><td>'modula3'</td><td>Modula 3</td></tr>
<tr><td>'68000devpac'</td><td>Motorola 68000 HiSoft Dev</td></tr>
<tr><td>'mpasm'</td><td>MPASM</td></tr>
<tr><td>'mxml'</td><td>MXML</td></tr>
<tr><td>'mysql'</td><td>MySQL</td></tr>
<tr><td>'newlisp'</td><td>newLISP</td></tr>
<tr><td>'text'</td><td>None</td></tr>
<tr><td>'nsis'</td><td>NullSoft Installer</td></tr>
<tr><td>'oberon2'</td><td>Oberon 2</td></tr>
<tr><td>'objeck'</td><td>Objeck Programming Language</td></tr>
<tr><td>'objc'</td><td>Objective C</td></tr>
<tr><td>'ocaml-brief'</td><td>OCalm Brief</td></tr>
<tr><td>'ocaml'</td><td>OCaml</td></tr>
<tr><td>'pf'</td><td>OpenBSD PACKET FILTER</td></tr>
<tr><td>'glsl'</td><td>OpenGL Shading</td></tr>
<tr><td>'oobas'</td><td>Openoffice BASIC</td></tr>
<tr><td>'oracle11'</td><td>Oracle 11</td></tr>
<tr><td>'oracle8'</td><td>Oracle 8</td></tr>
<tr><td>'oz'</td><td>Oz</td></tr>
<tr><td>'pascal'</td><td>Pascal</td></tr>
<tr><td>'pawn'</td><td>PAWN</td></tr>
<tr><td>'pcre'</td><td>PCRE</td></tr>
<tr><td>'per'</td><td>Per</td></tr>
<tr><td>'perl'</td><td>Perl</td></tr>
<tr><td>'perl6'</td><td>Perl 6</td></tr>
<tr><td>'php'</td><td>PHP</td></tr>
<tr><td>'php-brief'</td><td>PHP Brief</td></tr>
<tr><td>'pic16'</td><td>Pic 16</td></tr>
<tr><td>'pike'</td><td>Pike</td></tr>
<tr><td>'pixelbender'</td><td>Pixel Bender</td></tr>
<tr><td>'plsql'</td><td>PL/SQL</td></tr>
<tr><td>'postgresql'</td><td>PostgreSQL</td></tr>
<tr><td>'povray'</td><td>POV-Ray</td></tr>
<tr><td>'powershell'</td><td>Power Shell</td></tr>
<tr><td>'powerbuilder'</td><td>PowerBuilder</td></tr>
<tr><td>'proftpd'</td><td>ProFTPd</td></tr>
<tr><td>'progress'</td><td>Progress</td></tr>
<tr><td>'prolog'</td><td>Prolog</td></tr>
<tr><td>'properties'</td><td>Properties</td></tr>
<tr><td>'providex'</td><td>ProvideX</td></tr>
<tr><td>'purebasic'</td><td>PureBasic</td></tr>
<tr><td>'pycon'</td><td>PyCon</td></tr>
<tr><td>'python'</td><td>Python</td></tr>
<tr><td>'q'</td><td>q/kdb+</td></tr>
<tr><td>'qbasic'</td><td>QBasic</td></tr>
<tr><td>'rsplus'</td><td>R</td></tr>
<tr><td>'rails'</td><td>Rails</td></tr>
<tr><td>'rebol'</td><td>REBOL</td></tr>
<tr><td>'reg'</td><td>REG</td></tr>
<tr><td>'robots'</td><td>Robots</td></tr>
<tr><td>'rpmspec'</td><td>RPM Spec</td></tr>
<tr><td>'ruby'</td><td>Ruby</td></tr>
<tr><td>'gnuplot'</td><td>Ruby Gnuplot</td></tr>
<tr><td>'sas'</td><td>SAS</td></tr>
<tr><td>'scala'</td><td>Scala</td></tr>
<tr><td>'scheme'</td><td>Scheme</td></tr>
<tr><td>'scilab'</td><td>Scilab</td></tr>
<tr><td>'sdlbasic'</td><td>SdlBasic</td></tr>
<tr><td>'smalltalk'</td><td>Smalltalk</td></tr>
<tr><td>'smarty'</td><td>Smarty</td></tr>
<tr><td>'sql'</td><td>SQL</td></tr>
<tr><td>'systemverilog'</td><td>SystemVerilog</td></tr>
<tr><td>'tsql'</td><td>T-SQL</td></tr>
<tr><td>'tcl'</td><td>TCL</td></tr>
<tr><td>'teraterm'</td><td>Tera Term</td></tr>
<tr><td>'thinbasic'</td><td>thinBasic</td></tr>
<tr><td>'typoscript'</td><td>TypoScript</td></tr>
<tr><td>'unicon'</td><td>Unicon</td></tr>
<tr><td>'uscript'</td><td>UnrealScript</td></tr>
<tr><td>'vala'</td><td>Vala</td></tr>
<tr><td>'vbnet'</td><td>VB.NET</td></tr>
<tr><td>'verilog'</td><td>VeriLog</td></tr>
<tr><td>'vhdl'</td><td>VHDL</td></tr>
<tr><td>'vim'</td><td>VIM</td></tr>
<tr><td>'visualprolog'</td><td>Visual Pro Log</td></tr>
<tr><td>'vb'</td><td>VisualBasic</td></tr>
<tr><td>'visualfoxpro'</td><td>VisualFoxPro</td></tr>
<tr><td>'whitespace'</td><td>WhiteSpace</td></tr>
<tr><td>'whois'</td><td>WHOIS</td></tr>
<tr><td>'winbatch'</td><td>Winbatch</td></tr>
<tr><td>'xbasic'</td><td>XBasic</td></tr>
<tr><td>'xml'</td><td>XML</td></tr>
<tr><td>'xorg_conf'</td><td>Xorg Config</td></tr>
<tr><td>'xpp'</td><td>XPP</td></tr>
<tr><td>'yaml'</td><td>YAML</td></tr>
<tr><td>'z80'</td><td>Z80 Assembler</td></tr>
<tr><td>'zxbasic'</td><td>ZXBasic</td></tr>
</table> 
