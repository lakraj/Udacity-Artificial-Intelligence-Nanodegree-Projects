import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    #For each index in test set
    for i in range(test_set.num_items):
        #None did not work for placeholder, hence using ""
        best_wordguess = ""
        best_prob = float("-inf")
        word_prob = {}
        X, X_lengths = test_set.get_item_Xlengths(i)
        # Check each  word and corresponding model. Select the word with the highest probability/score. 
        for word, model in models.items():
            try:
                word_prob[word] = model.score(X, X_lengths)
            except:
                word_prob[word] = float("-inf")
            
            if word_prob[word] > best_prob:
                best_wordguess = word
                best_prob = word_prob[word]
        probabilities.append(word_prob)
        guesses.append(best_wordguess)
    return probabilities, guesses
            
