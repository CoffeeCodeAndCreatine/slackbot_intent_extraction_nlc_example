# nlc_trainer
This is a basic example of how to an NLC to extract intent from utterances for the use of a slack bot.

## Main Features
1. Train a model, and test model against test utterances  

## Explanation of Files
1. nlc_trainer.py: Source code to train and test the model
2. nlc_train_set.json: Set of data used to train the model
3. nlc_test_set.json: Set of data used to test the model
4. config_spacy.yml: Bare bones config for spacy
5. requirements.txt: List of requirements for pip

## How to Run
This sample is pretty straight forward, just run the main file, which will train and test a model. The model itself is trained off the nlc_train_set which is just a simple utterance set to turn on and off a light. 

1. First you will need to run pip to install the requirements.
    ```bash
    pip3 install -r requirements.txt
    ```
2. After pip, you will need to install the en lib for spacy
    ```bash
    python3 -m spacy download en
    ```
3. Once all the requirements and libs are installed you can run the main program.
    ```bash
    python3 nlc_trainer.py
    ```

## Sample Output
A sample output of the program is as follows.
```bash
    1) Configuring the model training
    2) Training the model
    Fitting 2 folds for each of 6 candidates, totalling 12 fits
    [Parallel(n_jobs=1)]: Done  12 out of  12 | elapsed:    0.0s finished
    3) Saving the model
    4) Loading up the model
    5) Loading up the test set
    6) Testing the model
    6) Printing model results
        PASSED
        utterance: light on
        intent: light_on
        light_on : 0.8161785372594302
    
        PASSED
        utterance: light on please
        intent: light_on
        light_on : 0.7207668675518358
    
        PASSED
        utterance: please turn on the light
        intent: light_on
        light_on : 0.7363085358390637
    
        PASSED
        utterance: light off
        intent: light_off
        light_off : 0.846485019174016
    
        PASSED
        utterance: light off please
        intent: light_off
        light_off : 0.8334535650778456
    
        PASSED
        utterance: please turn off the light
        intent: light_off
        light_off : 0.7554183740631956
    
    
    total test cases: 6
    passing rate: 100.0%
    failing rate: 0.0%
```

## How to add a new utterance
1. Open the nlc_test_set.json and add in json entries for a new utterance
2. Open the nlc_test_set.json and add in json entries for similar utterances (the test set and train set should be unique)
3. Rerun the nlc_trainer.py


## How To Video
[Coming Soon]()