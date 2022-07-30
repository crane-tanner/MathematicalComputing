import nltk 
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer 
stemmer = LancasterStemmer(0)

import numpy 
import tflearn
import tensorflow 
import random 
import json 
import pickle 

with open("intents.json") as file: 
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f: 
        words,labels,training,output = pickle.load(f)

except:
    words = [] 
    labels = []
    docs_x = [] 
    docs_y = []

    for intent in data["intents"]: # loop through all of the dictionaries in intents.json 
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern) # start stemming, or take each words root 
            words.extend(wrds)
            docs_x.append(wrds) # each entry in docs_x corresponds to each entry in docs_y 
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))] #output list of length of amount of labels we have 

    for x, doc in enumerate(docs_x):
        bag = [] #bag of encoded words 
        wrds = [stemmer.stem(w) for w in doc] #stem all the words in the pattern 

        for w in words: 
            if w in wrds:
                bag.append(1) # putting 1 if word exists
            else: 
                bag.append(0) # putting 0 if word does not exist

        output_row = list(out_empty[:])
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row) # the above code from here essentially gives a bunch a bags of words and gets data ready to feed into model

    training = numpy.array(training)
    output = numpy.array(output) # take the lists and change into arrays 

    with open("data.pickle", "wb") as f: 
        pickle.dump((words,labels,training,output), f ) 

tensorflow.compat.v1.reset_default_graph() #start building machine learning model

net = tflearn.input_data(shape = [None, len(training[0])]) #length of training data 
net = tflearn.fully_connected(net,8) # number of "neurons"
net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax") #generate probabilities for each neuron in layer using softmax
net = tflearn.regression(net)

model = tflearn.DNN(net)

#try:
model.load("model.tflearn")

#except:
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True) # pass in training data and have model read certain number of times 
model.save("model.tflearn")

def bag_of_words(s,words):
    bag = [ 0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words: #generate bag list 
        for i, w in enumerate(words):
            if w == se: 
                bag[i] = 1

    return numpy.array(bag)  # take bag of words convert to numpy array and return where needed 

def chat(): 
    print("Start talking with the bot (type quit to stop)!")
    while True: 
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])[0] # get models response to user input 
        results_index = numpy.argmax(results) # pick index of largest number
        tag = labels[results_index] # give label that model thinks user message is 

        if results[results_index] > 0.7: # if results greater than 70% confidence
            for tg in data["intents"]:
                if tg['tag'] == tag: 
                    responses = tg['responses']

            print(random.choice(responses)) #chat function returns list of probabilities 
            # and prints a response to what it thinks is appropiate to user question

        else:
            print("I didn't get that. Please try again.")

chat() #initiating chat function 




