### Introduction
One of the research question of WP3.3 is: How is spoken text of characters of ruling class (royality, nobility, gentry) and lower classes — especially of servants and jesters — related to each other? Can this relationship be quantitatively recorded algorithmically, and is a recurring pattern discernible? In order to facilitate researchers answering such questions [*Language Resource Switchboard*](https://switchboard.clarin.eu) has been created which has two key functions: [*UDPipe*](http://ufal.mff.cuni.cz/udpipe) has been used with texts of French, English and Spanish Baroque drama. [*UDPipe*](http://ufal.mff.cuni.cz/udpipe) is an trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files.
### Two ways two start
**Mind:** For some tools it can be helpful presenting solely plain text files instead of data already anyhow tagged.
Start by going to [*Language Resource Switchboard*](https://switchboard.clarin.eu) and take one of two following options:
![1. One of two following options](https://github.com/subugoe/factsheets_sshoc_services/tree/master/images/00switchboardHomepage.png)
_1. One of two following options_
1.  Either a researcher is already familiar with tools offered and know what is best to use answering research question or
2.  he or she wishes a pre-selection of tools best fitting.
If *1.* researcher can select tools by him- or herself clicking on Tool inventory choosing wished and afterwards finds a three ways function:
1.  uploading a file,
2.  submitting an ULR or
3.  submitting text.
If *2.* he or she may simple type in [https://switchboard.clarin.eu/input](https://switchboard.clarin.eu/input) in address bar of a browser and is facing three ways function, mentioned above.
### Which file formats and languages
By dragging a simple plain text file into field *Upload File* one can learn which *Mediatype* (file formats) and *Language(s)* are excluded from processing in general. Eg. both *x-mobipocket-ebook* and *xhtml+xml* are not supported whilst PDF is supported.
**Mind:** That a file format is not excluded completely does not mean that it can be processed with all possible tools thus it is highly recommended converting files into plain text, beforehand, if possible and no critical information will be lost.
### Usage
In order to use [*UDPipe*](http://ufal.mff.cuni.cz/udpipe) [Upload files or text](https://switchboard.clarin.eu/input) has been clicked on and plain text file of Spanish drama *A Dios por razón de estado* by Pedro Calderón de la Barca has been dragged onto field *Upload File*. Selection of four matching tools will be shown, videlicet for dependency parsing *UDPipe*, *Voyant Tools* for distant reading, for NER *NLP-HUB* and *WebLicht Advanced Mode* for text analytics. Different to this following 16 tools are shown after upload of William Shakespeare's *Cymbeline* as plain text file:
-   For constituency parsing *WebLicht Const Parsing*,
-   for dependency parsing three,
1.  *Spacy* (hosted by D4Science) - EN
2.  *UDPipe*
3.  *WebLicht Dep Parsing EN*,
-   for distant reading *Voyant Tools*,
-   for lemmatization
1.  *CSTLemma* (hosted by D4Science) and
2.  *WebLicht Lemmas EN*,
-   for machine translation *LINDAT Translation*,
-   a morpho-syntactic tagger called *Tagger NLTK*,
-   for morphological analysis *WebLicht Morphology EN*,
-   for Named Entity Recognition three,
1.  *NER NLTK*
2.  *NLP-HUB (multiple NER tools)*
3.  *WebLicht NamedEntities EN*,
-   a POS tagger named *WebLicht POSTags Lemmas EN*,
-   Text Analytics with *WebLicht Advanced Mode* and
-   for Text Enhancement *Distanbol*.
By clicking on *Open* *UDPipe* this application starts in a new tab window and spanish model for text processing is offered and processing is starting automatically. By clicking on *Advanced Options* further adjustments are possible and a new processing by clicking on button *Process input* is possible. Output both becomes visible in separate frame in tab window and can be downloaded as file in conllu format which is similar to a csv file.
