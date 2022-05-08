from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
from tensorflow import Graph
import tensorflow as tf
from django.conf import settings
import os
from rest_framework.response import Response
import numpy as np

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        animalmodel = load_model('./models/MobileNetModelImagenet.h5')
        # similaritymodel = load_model("")

valid_animals = [
                "antelope", "cockroach", "eagle", "hare", "lion", "oyster", "rhinoceros", "tiger",
                "badger","cow","elephant","hedgehog","lizard","panda", "seahorse", "turkey",
                "bat",          "coyote",     "flamingo",     "hippopotamus",  "lobster",   "parrot",     "seal",        "wolf",
                "bear",         "crab",       "fly",          "hornbill",      "mosquito",  "penguin",    "shark",       "wombat",
                "bee",          "crow",       "fox",          "horse",         "moth",      "pig",        "sheep",       "woodpecker",
                "beetle",       "deer",       "goat",         "hummingbird",   "mouse",     "pigeon",     "snake",       "zebra",
                "bison",        "dog",        "goldfish",     "hyena",         "octopus",   "porcupine",  "sparrow",
                "butterfly",    "dolphin",    "goose",        "jellyfish",     "okapi",     "possum",     "squid",
                "cat",          "donkey",     "gorilla",      "kangaroo",      "otter",     "raccoon",    "squirrel",
                "caterpillar",  "dragonfly",  "grasshopper",  "koala",         "owl",       "rat",        "starfish",
                "chimpanzee",   "duck",       "hamster",      "leopard",       "ox",        "reindeer",   "swan",
            ]

def _preprocess_image(file):
    fs = FileSystemStorage()
    filepathname = fs.save(file.name, file)
    filepathname = fs.url(filepathname)
    testimage =  '.' + filepathname
    img = image.load_img(testimage, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255
    x = x.reshape(1, 224, 224, 3)
    return x, filepathname

def _predict_scores(x):
    with model_graph.as_default():
        with tf_session.as_default():
            p = animalmodel.predict(x)
    return p

def _get_top_scores(p, n=5):
    import json
    scores = {}
    with open(os.path.join("models", "animal_labels.json")) as f:
        js = json.load(f)
        while n > 0:
            index = np.argmax(p)
            animal = js.get(str(index))[1].lower().split("_")
            for a in animal:
                if a in valid_animals and a not in scores:
                    n -= 1
                    scores[a] = p[index]
                    break
            p[index] = -1
            
    return scores

def predict_similarity_scores(image):
    x, path = _preprocess_image(image)
    p = _predict_scores(x)
    scores = _get_top_scores(p[0])
    
    return scores, path

def calculate_similarities(anchor, *positives):
    # result = []
    # for p in positives:
    #     r = similaritymodel.predict((p, anchor))
    #     result.append(r[0][0], p.url)
    return positives[0].url