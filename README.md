# SpellCorrection Lambda
The purpose of this project was to focus on learning the fundamentals of serverless methods by setting up a serverless project,writing my first Lambda function in Python and deploying to AWS. 

This function takes a dictionary as input, with the key 'word' and any string value representing a word.\
When invoked it returns a string value with the most probable correct spelling.


## Serverless Framework
Install Serverless framework globally:

````
npm install -g serverless

````


## Run locally
In order to run the function locally you need to install the requirements:

``` bash
$ pip install -r requirements.txt

```

After completed installation you can invoke the function locally:

```
$ serverless invoke local --function correct_word -d '{"word": "[some_misspelled_word]" }'

```


## Deploy and invoke
Set up your AWS credentials and deploy:

``` bash
$ serverless deploy

```
Invoke the function:
```
$ serverless invoke --function correct_word -d '{"word": "[some_misspelled_word]" }'

```
