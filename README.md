# Python Workshop

Web interface with model that predicts survivors of Titanic crash. 


## Setup

### Installation
Access CIBC Data Studio - python-workshop Git repository to pull all the relevant application codes and files.

First, create a folder named "python-workshop" to clone the repository.

Then run this:

1) Clone the git repository
```shell
git clone https://github.com/CIBCDataStudio/python-workshop.git
```
2) Go into the python-workshop folder
```shell
cd python-workshop
```

3) Check status to see if the repo has succesfully been cloned.
```shell
git status
```



#### Install dependencies

To install Python dependencies, run:

```shell
pip install -r requirements.txt
```


#### Running the application

Inside the python-workshop folder from the git repo, run the following:
```shell
python ./run.py
```


### Running the server

Go to http://40.84.53.8:5000/ for the application.


## Code Setup

### Config File Description
<p>[UploadFolders]: These are the names of the temporary folders that handle the uploaded files from the website.<br>

[DownloadFolders]: These are the names of the temporary folders that handle the downloaded files from the website.<br>

[PickleFileName]: The name of the model class pickle file.<br>

[NeuralNetConfig]: This tag sets the parameters of the neural network structure.<br>

[Misc]: This tag sets the additional parameters used in the machine learning model.<br>

### Classes used
<ul>
<li> NN_model - Holds all methods used by the neural network model class and the model.
<li> RR_model - Holds all methods used by the random forest model class and the model.
</ul>
