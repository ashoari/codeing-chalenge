# Table of Contents

1. [Environement and Settings] (README.md#Environement and Settings)
2. [Repository Structure] (README.md#Repository structure)
3. [Testing Directory] (README.md#Testing Directory)

This file explains the procedures and environment settings for implementation of Insight Venmo project. The project aimed to calculate the median degree of a vertex in a graph and update this each time a new Venmo payment appears. The time-frame for median calculation is considered to be 60-seconds.


##Environement and Settings
[Back to Table of Contents] (README.md#table-of-contents)
Our code has been developed with Python 3.5. All the libraries used are standard library but statistics library is not available on Python 2.7. Thus the run.sh code is changes to emphasise that the code should be run in release 3. The code has been tested on cloud9 Linux shell and it works fine. To do the testing I changed the permission of both `run.sh` and `run_tests.sh` shell scripts to be executable using `chmod u+x` command. Also `run_tests.sh` has been executed from its main directory using `./run_tests.sh` command and passed all three tests. Please note that I assume that the float value of median degree use two decimal digits as used in the provided test example and project description. If the output in the test vector does not follow the same convention, the test_script may not pass even with numerical identical outputs.

##Repository Structure
[Back to Table of Contents] (README.md#table-of-contents)

I used similar structure provided in the project decription with some minor modification as follows:
1- A folder called "JupiterNotebook" has been added. This folder keeps my Jupiter Notebook source code which I keep for future reference but has nothing to do with the chalenge submission.
2- Two additional test vectors has been added to the "tests" folder.  


	├── README.md 
	├── run.sh
	├── src
	│  	└── median_degree.py
	├── images (not being used)
	├── JupiterNotebook (not being used)
	├── data-gen   (input and output for all transaction source)
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


The algorithm used is as following:




Everytime a new transaction arrive
1- update the maxtimestamp
2- If the transaction is less than 60 seconds away from the maxtimestamp, ignore new entrance and go forward by repeating the previous output and write it in the output file
3- If not, calculate the new set of transin60 list of list. Go through the previous transactions and remove the ones outside order. append the new transaction at the end of the record.
4- Create (Update is hard to know the effect of removed edges) the list of collection dictionary of lists based on  transin60
5- Build a degree dictionary for all nodes which relates them with their integer degree.
6- Create a list of non-zero items in degree dictionary.
7- Run medium function over the sorted version of ths list. 
8- Write the output in a new line in output file.
