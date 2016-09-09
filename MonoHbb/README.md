# MonoH

-- MonoHBranchReader.py can be used to run on one rootfile and it gives back one rootfile with signal region histograms and text file with efficiency. 

-- This efficiency info will be in rootfile in future. 

python MonoHBranchReader.py -a -i rootfilename

# Run on all samples

-- MonoHbbAllSamplesReader.py will loop over all the filrs listed in in text file: allfiles.txt and run the MonoHBranchReader.py script on all these files one by one. 

-- Run it using 

python MonoHbbAllSamplesReader.py


-- For signal region use: 

python MonoHBranchReader.py  -m 100 -M 150 -i NCUGlobalTuples_1.root  -a -j 0 -J 2 -l 0 -L 1