import spacy
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Interpreter
from rasa_nlu.model import Trainer
import json


print("1) Configuring the model training")
train_data = load_data('nlc_train_set.json')
trainer = Trainer(config.load("config_spacy.yml"))

print("2) Training the model")
trainer.train(train_data)

print("3) Saving the model")
model_directory = trainer.persist('projects/')

print("4) Loading up the model")
nlp = spacy.load('en')
interpreter = Interpreter.load(model_directory)

print("5) Loading up the test set")
test_utterances = []
with open('nlc_test_set.json') as json_data:
    test_utterances = json.load(json_data)

print("6) Testing the model")
total = len(test_utterances)
passed = 0
failed = 0
print_fails = True
print_passes = True

print("6) Printing model results")
output = []
for utt in test_utterances:
    results = interpreter.parse(utt['text'])
    tmp = {}
    tmp['utterance'] = utt['text']
    tmp['target_intent'] = utt['intent']
    tmp['calculated_intent'] = results['intent']['name']
    tmp['intent_score'] = results['intent']['confidence']
    output.append(tmp)
    if results['intent']['name'] == utt['intent']:
        passed = passed + 1
        if print_passes:
            print("\tPASSED")
            print("\tutterance: " + utt['text'])
            print("\tintent: " + utt['intent'])
            print("\t" + str(results['intent']['name'] + " : " + str(results['intent']['confidence'])) + "\n")
    else:
        if print_fails:
            print("\tFAILED")
            print("\tutterance: " + utt['text'])
            print("\tintent: " + utt['intent'])
            print("\t" + str(results['intent']['name'] + " : " + str(results['intent']['confidence'])) + "\n")

        failed = failed + 1

print("\ntotal test cases: " + str(total))
print("passing rate: " + str(100*(passed/total)) + "%")
print("failing rate: " + str(100*(failed/total)) + "%")