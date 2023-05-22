# AlgorithmEngineering_SS23

## Blatt 2
### Problem 1: Solution Checker

- Im Ordner CVRP einen Ordner "data" erstellen, die [CVRPLib](http://vrp.galgos.inf.puc-rio.br/index.php/en/) Files von Uchoa et al. (2014) und Arnold, Gendreau, and Sorensen (2017) herunterladen und dort entpacken, die einzelnen Files aus den Subfoldern raus in den jeweils äußersten Folder kopieren (einfacherer Pfad)
- cvrp_SolutionChecker mit cmake bauen, dann zum testen:
```
$ ./cvrp_SolutionChecker ../data/Vrp-Set-X/X-n101-k25.vrp ../data/Vrp-Set-X/X-n101-k25.sol
``` 
und 
```
$ ./cvrp_SolutionChecker ../data/Vrp-Set-XXL/Ghent1.vrp ../data/Vrp-Set-XXL/Ghent1.sol
``` 

### Problem 2: Greedy Heuristic
- Executable `greedy_cvrp` mit cmake bauen, dann zum testen: 
```
$ ./greedy_cvrp ../data/Vrp-Set-X/X-n101-k25.vrp
``` 
- Leider bekommen wir momentan immer einen `segmentation fault` und konnten bisher noch nicht rausfinden, warum.