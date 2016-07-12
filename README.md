# Table of Contents

1. [Environement and Settings] (README.md#Environement and Settings)
2. [Repository Structure] (README.md#Repository structure)
3. [Testing Directory] (README.md#Testing Directory)
4. [Algorithm Summary] (README.md#Algorithm Summary)

This file explains the procedures and environment settings for implementation of Insight Venmo project. The project aimed to calculate the median degree of a vertex in a graph and update this each time a new Venmo payment appears. The time-frame for median calculation is considered to be 60-seconds.


##Environement and Settings
[Back to Table of Contents] (README.md#table-of-contents)
My code has been developed with Python 3.5. All the libraries used are standard library but statistics library is not available on Python 2.7. Thus the run.sh code is changes to emphasise that the code should be run in release 3. The code has been tested on cloud9 Linux shell and it works fine. To do the testing I changed the permission of both `run.sh` and `run_tests.sh` shell scripts to be executable using `chmod u+x` command. Also `run_tests.sh` has been executed from its main directory using `./run_tests.sh` command and passed all three tests. Please note that I assume that the float value of median degree use two decimal digits as used in the provided test example and project description. If the output in the test vector does not follow the same convention, the test_script may not pass even with numerical identical outputs.

##Repository Structure
[Back to Table of Contents] (README.md#table-of-contents)

I used similar structure provided in the project decription with some minor modification as follows:

1- A folder called "JupiterNotebook" has been added. This folder keeps my Jupiter Notebook source code which I keep for future reference but has nothing to do with the chalenge submission.

2- Two additional test vectors have been added to the "tests" folder.  


	├── README.md 
	├── run.sh
	├── src
	│  	└── median_degree.py
	├── images (not being used)
	├── JupiterNotebook (not being used)
	├── data-gen   (input and output for all transactions)
	│  	└── venmo-trans.txt
	│  	└── output.txt
	├── venmo_input
	│   └── venmo-trans.txt
	├── venmo_output
	│   └── output.txt
	└── insight_testsuite
	 	   ├── run_tests.sh
		   └── tests
	        	└── test-1-venmo-trans
        		│   ├── venmo_input
        		│   │   └── venmo-trans.txt
        		│   └── venmo_output
        		│       └── output.txt
        		└──test-2-venmo-trans
        		│   ├── venmo_input
        		│   │   └── venmo-trans.txt
        		│   └── venmo_output
        		│       └── output.txt
        		│──test-3-venmo-trans
        		     ├── venmo_input
        	             │   └── venmo-trans.txt
        		     └── venmo_output
        		         └── output.txt

The contents of `src` contains the single Python 3.5 source code called `rolling_median.py`. 

##Testing Directory
[Back to Table of Contents] (README.md#table-of-contents)

-"test-1-venmo-trans" is the test vector provided by Insight. 

-"test-2-venmo-trans" is simply a test vector based on the graphical example provided in the project description i.e.
  The payment's information is :

	actor = Jordan-Gruber,	 	target = Jamie-Korn, 		created_time: 2016-04-07T03:33:19Z
	actor = Maryann-Berry, 		target = Jamie-Korn, 		created_time: 2016-04-07T03:33:19Z
	actor = Ying-Mo, 			target = Maryann-Berry, 	created_time: 2016-04-07T03:33:19Z
	actor = Jamie-Korn, 		target = Ying-Mo, 			created_time: 2016-04-07T03:34:18Z
	actor = Maryann-Berry, 		target = Maddie-Franklin, 	created_time: 2016-04-07T03:34:58Z
	actor = Maryann-Berry, 		target = Ying-Mo, 			created_time: 2016-04-07T03:34:00Z
	actor = Natalie-Piserchio, 	target = Rebecca-Waychunas, created_time: 2016-04-07T03:31:18Z
	actor = Nick-Shirreffs, 	target = Connor-Liebman, 	created_time: 2016-04-07T03:35:02Z

   And the output median degree as :

	1.00
	1.00
	1.50
	2.00
	1.00
	1.50
	1.50
	1.00

-"test-3-venmo-trans" is similar to "test-2-venmo-trans" but 4 additional corrupted transactions with empty "actor" fields have been added to the input (one at the beginning of the input stream and the others at the end). We know that the output should be the same as the output of "test-2-venmo-trans" but some error messages will be communicated to the console.


##Algorithm Summary
[Back to Table of Contents] (README.md#table-of-contents)

The algorithm used is as following:

1-Everytime a new transaction arrives, extract the date-time-stamp of the transaction in addition to the names of the 'target' and 'actor' of the transaction.

2-If any of the above mentioned field is empty, ignore the transaction and communicate an error message to the console and go back to step 1 to read the next transaction.

3-If the record does contain all the elements, first update the maximum-time-stamp based on previous maximum-time-stamp and the current received transaction.

	3-1-If the current transaction time stamp is within 60s from the maximum-time-stamp, update the list `TranLast60` by adding the current transaction at the bottom of the list and removing all the previous transactions in `TranLast60` which are no longer within 60s timeframe from the current maximum-time-stamp.
	
	3-2 Otherwise, do not update the `TranLast60` and use previous values.
	
4-Build a dictionary of lists called `graph` based on the records appearing in `TranLast60`.

5-Since the list corresponding to each vertex may contain repeated elements, use the number of elements of the set resulted from that list to calculate the degree of each vertex. Store the calculated degree in a new dictionary composed of the vertices' names and their corresponding degrees.

6- Make a list out of the dictionary `degree`, sort the list and use median function from statistics library of Python3 to calculate the output.

7- Write the output to the end of the output file and go back to step 1 until no additional record left in the input file.


