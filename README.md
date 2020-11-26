# MitoFish2tbl
Convert MitoAnnotator (MitoFish) annotation file to NCBI feature table format (\*.tbl)

The script `mitofish2tbl.py` was developed and tested with Python 2.7.12 and is part of the supplementary material of the article __Global systematic diversity, range distributions, conservation and taxonomic assessments of graylings (Teleostei: Salmonidae; Thymallus spp.)__ by Steven J. Weiss, et al. 2020. _Organisms Diversity and Evolution_. doi: [10.1007/s13127-020-00468-7](https://doi.org/10.1007/s13127-020-00468-7)

## Testdata

The directory testdata contains annotation results obtained from the Mitofish annotation pipeline ([link](http://mitofish.aori.u-tokyo.ac.jp/annotation/input.html), last accessed 26.11.2020). The original DNA sequence submitted is in the file `testdata/Thy10.fa`. 

## Usage

The script takes exactly one input file (mitoannotator annotation file, e.g. `annotation.txt`) and produces one output file (annotation in `tbl` format, e.g. `annotation.tbl`). Per default the output file will have the same prefix as the input txt file and will be written to the same location as the input file. 

Try it, like so:
```bash
(host)-$ ./mitofish2tbl.py testdata/Thy10.txt 
mitofish file to convert: testdata/Thy10.txt
writing to: testdata/Thy10.tbl
```

