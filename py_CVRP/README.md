# AlgorithmEngineering_SS23


## Blatt 2
### Problem 1: Solution Checker

*Tip:* Im übergeordneten Ordner einen Ordner "data" erstellen, die [CVRPLib](http://vrp.galgos.inf.puc-rio.br/index.php/en/) Files von Uchoa et al. (2014) und Arnold, Gendreau, and Sorensen (2017) herunterladen und dort entpacken, die einzelnen Files aus den Subfoldern raus in den jeweils äußersten Folder kopieren (einfacherer Pfad)

Dann sieht die Eingabe zum Testen so aus:
```
$ python3 solution_checker.py ../data/Vrp-Set-X/X-n101-k25.vrp ../data/Vrp-Set-X/X-n101-k25.sol
``` 
und 
```
$ python3 solution_checker.py ../data/Vrp-Set-XXL/Ghent1.vrp ../data/Vrp-Set-XXL/Ghent1.sol
``` 

### Problem 2: Greedy Heuristic
```
$ python3 greedy_heuristic.py ../data/Vrp-Set-X/X-n101-k25.vrp
``` 
