<h3>Introduction</h3>
<p>One of the research question of WP3.3 is: How is spoken text of characters of ruling class (royality, nobility, gentry) and lower classes — especially of servants and jesters — related to each other? Can this relationship be quantitatively recorded algorithmically, and is a recurring pattern discernible? In order to facilitate researchers answering such questions <a href="https://switchboard.clarin.eu/tools" target="_blank">
<i>Language Resource Switchboard</i></a> has been created which has two key functions:
<a href="http://ufal.mff.cuni.cz/udpipe" target="_blank">
<i>UDPipe</i></a> has been used with texts of French, English and Spanish Baroque drama. <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank">
<i>UDPipe</i></a> is an trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files.</p> 
<h3>Two ways two start</h3>
<p>
<b>Mind:</b> For some tools it can be helpful presenting solely plain text files instead of data already anyhow tagged.</p>
<p>Start by going to <a href="https://switchboard.clarin.eu" target="_blank">
<i>Language Resource Switchboard</i></a>[languageResourceSwitchboard.png] and take one of two following options:</p>
![1. Browsing the VCR](images/01toolInventory.png)
_1. Browsing the VCR_

<i>1. Browsing the VCR_</i>
<ol>
<li>Either a researcher is already familiar with tools offered and know what is best to use answering research question or</li>
<li>he or she wishes a pre-selection of tools best fitting.</li>
</ol>
<p>If <i>a)</i> researcher can select tools by him- or herself clicking on <a href="https://switchboard.clarin.eu/tools" target="_blank">Tool inventory</a>[toolInventory.png] choosing wished and afterwards finds a three ways function:</p>
<ol>
<li>uploading a file,</li>
<li>submitting an ULR or </li>
<li>submitting text.</li>
</ol>
<p>If <i>b)</i> he or she may simple type in <a href="https://switchboard.clarin.eu/input" target="_blank">https://switchboard.clarin.eu/input</a>[uploadFilesOrText.png] in address bar of a browser and is facing three ways function, mentioned above:</p>
<ol>
<li>uploading a file,</li>
<li>submitting an ULR or </li>
<li>submitting text.</li>
</ol>
<h3>Which file formats and languages</h3>
<p>By dragging a simple plain text file into field <i>Upload File</i>[03uploadFile.png] one can learn which <i>Mediatype</i> (file formats) and <i>Language(s)</i> are excluded from processing in general. Eg. both <i>x-mobipocket-ebook</i> and <i>xhtml+xml</i> are not supported whilst PDF is supported.</p>
<p>
<b>Mind:</b> That a file format is not excluded completely does not mean that it can be processed with all possible tools thus it is highly recommended converting files into plain text, beforehand, if possible and no critical information will be lost.</p>
<h3>Usage</h3>
<p>In order to use <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank">
<i>UDPipe</i></a> <a href="https://switchboard.clarin.eu/input" target="_blank">Upload files or text</a> has been clicked on and plain text file of Spanish drama <i>A Dios por razón de estado</i> by Pedro Calderón de la Barca has been dragged onto field <i>Upload File</i> Selection of four matching tools will be shown, videlicet for dependency parsing <i>UDPipe</i>, <i>Voyant Tools</i> for distant reading, for NER <i>NLP-HUB</i> and <i>WebLicht Advanced Mode</i> for text analytics. Different to this following 16 tools are shown after upload of William Shakespeare's <i>Cymbeline</i> as plain text file:</p>
<ul>
<li>For constituency parsing <i>WebLicht Const Parsing</i>,</li>
<li>for dependency parsing three,
<ol>
<li><i>Spacy</i> (hosted by D4Science) - EN</li>
<li><i>UDPipe</i></li>
<li><i>WebLicht Dep Parsing EN</i>,</li>
</ol>
</li>
<li>for distant reading <i>Voyant Tools</i>,</li>
<li>for lemmatization
<ol>
<li><i>CSTLemma</i> (hosted by D4Science) and</li>
<li><i>WebLicht Lemmas EN</i>,</li>
</ol>
</li>
<li>for machine translation <i>LINDAT Translation</i>,</li>
<li>a morpho-syntactic tagger called <i>Tagger NLTK</i>,</li>
<li>for morphological analysis <i>WebLicht Morphology EN</i>,</li>
<li>for Named Entity Recognition three,
<ol>
<li><i>NER NLTK</i></li>
<li><i>NLP-HUB (multiple NER tools)</i></li>
<li><i>WebLicht NamedEntities EN</i>,</li>
</ol>
</li>
<li>a POS tagger named <i>WebLicht POSTags Lemmas EN</i>,</li>
<li>Text Analytics with <i>WebLicht Advanced Mode</i> and</li>
<li>for Text Enhancement <i>Distanbol</i>.</li>
</ul>
<p>By clicking on <i>Open</i> <i>UDPipe</i> application starts in a new tab window and spanish model for text processing is offered and processing is starting automatically. By clicking on <i>Advanced Options</i> further adjustments are possible and a new processing by clicking on button Process input is possible. Output both becomes visible in separate frame in tab window and can be downloaded as file in conllu format which is similar to a csv file.</p>