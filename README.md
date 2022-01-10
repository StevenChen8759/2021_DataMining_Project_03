# 2021_DataMining_Project_03
Data Mining Project for Link Analysis

# Report Link
https://hackmd.io/@StevenHHChen/DM2021_Project3_Steven


# Running This Repo
1. Clone this project to your Ubuntu environment (e.g. Ubuntu 20.04LTS, WSL-Ubuntu 20.04) or Windows Powershell
```shell
$ git clone ...
```
2. Ensure that you have already installed Python 3.8.x in your envioronment.
```shell
$ python -V
```
3. Install pipenv via `pip`
```shell
$ pip install pipenv
```
4. Run make command below to obtain the output.
    * If you run this repo in the Windows Powershell, please copy the command in the Makefile and run it following the order below.
    * The step `ibm_preprocess` will generate visualized graph by graphviz. This task takes a long time to accomplished due to the size of graph. After the file `ibm-5000_preprocessed.txt` has generated, you can click Control-C to interrupt this process and go to next step `run`.
    * The step `run` will finish in about 5 ~ 10 minutes.
    * Testing Environment Reference:
        * OS: Windows 10
        * Shell: Windows PowerShell
        * CPU: Intel Core i7-1185G7 @ 3.00GHz
        * Memory: 16GB
        * Storage: 1TB SSD
```shell
$ make init
...
$ make ibm_preprocess
...
$ make run
...
$ make graph_adjust
...
```
5. If you want to view-up repo within generated output files, run the git command below.
```
git checkout -b repo_with_output_files original/repo_with_output_files  # First time run, create local branch.
```
```
git checkout repo_with_output_files  # Branch already exists, checkout to this branch.
```
