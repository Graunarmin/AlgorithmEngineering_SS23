# AlgorithmEngineering_SS23


## Blatt 2
*Tip:* Im übergeordneten Ordner einen Ordner "data" erstellen, die [CVRPLib](http://vrp.galgos.inf.puc-rio.br/index.php/en/) Files von Uchoa et al. (2014) und Arnold, Gendreau, and Sorensen (2017) herunterladen und dort entpacken, die einzelnen Files aus den Subfoldern raus in den jeweils äußersten Folder kopieren (einfacherer Pfad)

### Problem 1: Solution Checker

Dann sehen mögliche Eingaben zum Testen so aus:
```
$ python3 solution_checker.py ../data/Vrp-Set-X/X-n101-k25.vrp ../data/Vrp-Set-X/X-n101-k25.sol
$ python3 solution_checker.py ../data/Vrp-Set-X/X-n599-k92.vrp ../data/Vrp-Set-X/X-n599-k92.sol
$ python3 solution_checker.py ../data/Vrp-Set-X/X-n1001-k43.vrp ../data/Vrp-Set-X/X-n1001-k43.sol
$ python3 solution_checker.py ../data/Vrp-Set-XXL/Ghent1.vrp ../data/Vrp-Set-XXL/Ghent1.sol
$ python3 solution_checker.py ../data/Vrp-Set-XXL/Antwerp2.vrp ../data/Vrp-Set-XXL/Antwerp2.sol
```

### Problem 2: Greedy Heuristic
```
$ python3 greedy_heuristic.py ../data/Vrp-Set-X/X-n101-k25.vrp
$ python3 greedy_heuristic.py ../data/Vrp-Set-X/X-n599-k92.vrp
$ python3 greedy_heuristic.py ../data/Vrp-Set-X/X-n1001-k43.vrp
$ python3 greedy_heuristic.py ../data/Vrp-Set-XXL/Ghent1.vrp
$ python3 greedy_heuristic.py ../data/Vrp-Set-XXL/Antwerp2.vrp
``` 

## Blatt 3
### Problem 1: Third Heuristic
Wir haben versucht, den Greedy-Approach aus Blatt 2 durch die Miteinbeziehung von Durchschnittsdistanzen zu verbessern.

Mögliche Eingaben zum Testen:

```
$ python3 average_distance_heuristic.py ../data/Vrp-Set-X/X-n101-k25.vrp
$ python3 average_distance_heuristic.py ../data/Vrp-Set-X/X-n599-k92.vrp
$ python3 average_distance_heuristic.py ../data/Vrp-Set-X/X-n1001-k43.vrp
$ python3 average_distance_heuristic.py ../data/Vrp-Set-XXL/Ghent1.vrp
$ python3 average_distance_heuristic.py ../data/Vrp-Set-XXL/Antwerp2.vrp
``` 