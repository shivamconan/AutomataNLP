# AutomataNLP
This project explores the possibility of automatically converting manual test cases to selenium automation.

Usage:

**For executing test steps in run time -**

Run the main.py file and write steps similar to this syntax -

1) Open chrome browser
2) Load www.xyz.com url
3) Enter/Type xyz in abc field
4) Click on/at (the) abc link/button
5) Hit/Press xyz key

This is acheieved using NLP(Natuaral Language Processing). NLTK is the library used. The algorithm is briefly explained as follows -

**First stage -** 

Tokenizing the sentence using default tokenizer in NLTK.

**Second stage -**

Tagging the tokenized words. Following custom tags are used -

1) Action (A) - Action which needs to be performed i.e. click, type, hit, open, etc.
2) Action Item Name (AIN) - The visible text of the web element user needs to perform action on.
3) Action Item Kind (AIK) - The kind of the action item element on which the action is supposed to be performed. Ex- button, link, etc.
4) Action Data (AD) - The data associated with the action. Ex - the data needed to be entered in a text field.
5) IN (preposition/subordinating conjunction : same as IN tag from nltk.pos_tag()) - Words like in,at, etc.
6) DT (Determiner : same as DT tag from nltk.pos_tag()) - the. 
 
Following features are considered to train the model to tag the words -

1) word itself
2) previous word
3) tag of previous word
4) next word

**Third stage -** 

Taking the tagged input and creating and then executing appropriate Selenium commands.

Here is a video of the project in action - https://www.youtube.com/watch?v=Da6uHIWtQyQ

