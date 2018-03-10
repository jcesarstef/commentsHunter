# commentsHunter
A simple Python script to hunt for HTML comments

# Usage
```
python3 commentsHunter.py --help
usage: commentsHunter.py [-h] --file FILE

commentsHunter. An simple script to hunt comments in URL's Created by
@jcesrstef.

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  File with URL's to scan, one per line.
```
  
```
cat urls.txt
http://baixaki.com.br
https://amazon.com
```
```
python3 commentsHunter.py --file urls.txt 

[+] 200 http://baixaki.com.br

<!-- Inicio da tag TT de segmencatao -->
<!-- Final da tag TT de segmentacao -->
<!-- Begin Digital Analytix Tag -->
<!-- End Digital Analytix Tag -->
<!-- Login -->
<!-- // Login -->
<!-- bxk_home_leaderboard -->
<!-- AEP br_nzn_baixaki_home_970x200_6ads_3 -->
<!-- /1010728/bxk_home_halfpage -->
<!-- bloco dos sites nas homes -->
[...]

[+] 200 https://amazon.com

<!-- sp:feature:head-start -->
<!-- sp:feature:cs-optimization -->
<!-- sp:feature:aui-assets -->
<!-- sp:feature:nav-inline-css -->
<!--  -->
<!-- sp:feature:host-assets -->
<!--&&&Portal&Delimiter&&&-->
<!-- sp:end-feature:host-assets -->
<!-- sp:feature:head-close -->
<!-- sp:feature:start-body -->
[...]
```
