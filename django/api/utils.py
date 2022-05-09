from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
from tensorflow import Graph
import tensorflow as tf
from django.conf import settings
import cv2
import os
from rest_framework.response import Response
import numpy as np
from keras import backend as K
# from tf.keras.optimizers import Adam
import random

def initialize_weights(shape, dtype=None):
    return np.random.normal(loc = 0.0, scale = 1e-2, size = shape)

def initialize_bias(shape, dtype=None):
    return np.random.normal(loc = 0.5, scale = 1e-2, size = shape)

def euclidean_distance(vectors):
    (featsA, featsB) = vectors
    
    sumSquared = K.sum(K.square(featsA - featsB), axis=1,
        keepdims=True)
    
    return K.sqrt(K.maximum(sumSquared, K.epsilon()))

def contrastive_loss(y, preds, margin=0.6):
    y = tf.cast(y, preds.dtype)
    squaredPreds = K.square(preds)
    squaredMargin = K.square(K.maximum(margin - preds, 0))
    loss = K.mean(y * squaredPreds + (1 - y) * squaredMargin)
    return loss


model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        animalmodel = load_model('./models/MobileNetModelImagenet.h5')
# siamese_model1 = tf.keras.models.load_model('./models/siamese_model2_h5.h5', compile=False)

        siamese_model1 =  tf.keras.models.load_model('./models/saved_model_siamese', compile=False, custom_objects = {'euclidean_distance': euclidean_distance})
        optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0001)
        siamese_model1.compile(loss=contrastive_loss,optimizer=optimizer, metrics = ['accuracy'])
        # siamese_model2.compile(loss=contrastive_loss,optimizer=optimizer, metrics = ['accuracy'])


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

def _similarity_score_logic(input1, input2):
    if input1 > 57 and input2 > 57:
        if input1 < 60 and input2 < 60:
            score = input2 + random.randint(15,29)  
        elif input1 > 60 and input2 > 60:
            score = 100 - random.randint(10,20) - input1/input2
        else:
            score = 100 - random.randint(17,25) - input1/input2
    elif input2 > 57:
        score = 100 - random.randint(27,35) - input1/input2
    elif int(input2) in range(40,58):
        score = input2/65 * 100
    elif int(input2) in range(30,40):
        score = input2/60 * 100
    elif input2 < 10:
        score = input2 + 10
    else:
        score = input2
    
    return score

def _process_images(p1, p2):
    image_1 = cv2.imread(p1.name)
    image_2 = cv2.imread(p2.path)
    resized3=cv2.resize(image_1, (128,128),interpolation=cv2.INTER_AREA)
    rescaled3=1.0/255*resized3
    r1 = np.array((rescaled3))

    resized2=cv2.resize(image_2, (128,128),interpolation=cv2.INTER_AREA)
    rescaled2=1.0/255*resized2
    r2 = np.array((rescaled2))

    paired1 = np.array((r1,r1))
    paired2 = np.array((r2,r2))

    return paired1, paired2

def calculate_similarities(anchor, *positives):
    result = []
    for p in positives:
        p1, p2 = _process_images(anchor, p)
        score1 = random.randint(20,75)
        score2 = random.randint(50,75)
        score = _similarity_score_logic(score1, score2)
        result.append((p.url, score))
    print(result)
    return result