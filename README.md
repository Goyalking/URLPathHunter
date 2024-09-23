# URLPathHunter
Its a powerfull automated tool web directory scanning tool design for cyber security Freshers and professionals to discover hidden directories and files on a target website with a customized wordlist and specified file extension.. It helps to identify vulnerabilities and exposed resources.
The URL Path Hunter tool is designed for educational and ethical purposes only.




Installation:
1. git clone https://github.com/Goyalking/URLPathHunter.git
2. cd URLPathHunter
3. chmod +x Hunter.py
4. dos2unix Hunter.py (This Command will Convert Hunter.py file to unix format to make it executable in Linux)
5. ./Hunter.py -t https://example.com/ -w wordlist.txt (-t Flag is used for target website and -w Flag Used for wordlist)




Things to Keep In Mind :
1. This tools will work in linux only.
2. For better results use your own customized wordlist or you can use Seclists etc.
3. This tool will provide you specific file (xml, json, sql, db, log, yml, yaml, bak, txt, tar.gz) results excluding http status code (301, 403, 404, 502, 503, 400, 500).
4. The tool is straightforward to use, making it accessible for beginners and experienced professionals alike.
