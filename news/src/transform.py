import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk import download
download('stopwords')
ps = PorterStemmer()
voc_size = 6000

def encode(str):
    review = re.sub('[^a-zA-Z]',' ',str)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    corpus = ' '.join(review)
    onehot_rep_test = [one_hot(corpus,voc_size)]
    encoded = pad_sequences(onehot_rep_test,padding='pre',maxlen=25)
    return encoded
