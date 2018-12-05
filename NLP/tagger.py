import nltk

class ConsecutivePosTagger(nltk.TaggerI):
    
    def get_features(self,sent,i,history):
         features = {"word" : None, "prev_word":None, "prev_tag":None, "next_word":None}
         features["word"] = sent[i]
         if i == 0:
                features["prev_word"] = "<START>"
                features["prev_tag"] = "<START>"
         else:
                features["prev_word"] = sent[i-1],
                features["prev_tag"] = history[i-1]
         if i == len(sent) - 1:
                features["next_word"] = "<END>"
         else:
                features["next_word"] = sent[i+1]
         #print features
         return features
	
    
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = self.get_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = self.get_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)
    
    