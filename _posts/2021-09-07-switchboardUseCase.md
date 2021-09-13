---
layout:     default
title:      Use Case Of Language Resource Switchboard
date:       2021-09-07T16:20:00Z
---        
<h2>Introduction</h2>
<p>One of the research question of WP3.3 is: How is spoken text of characters of ruling class (royality, nobility, gentry) and lower classes — especially of servants and jesters — related to each other? Can this relationship be quantitatively recorded algorithmically, and is a recurring pattern discernible? In order to facilitate researchers answering such questions <a href="https://switchboard.clarin.eu" target="_blank">Language Resource Switchboard</a> has been created which has two key functions: <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a> has been used with texts of French, English and Spanish Baroque drama. <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a> is an trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files.</p>
<h2>Two ways two start</h2>
<p><b>Mind:</b> For some tools it can be helpful presenting solely plain text files instead of data already anyhow tagged.</p>
<p>Start by going to <a href="https://switchboard.clarin.eu" target="_blank">Language Resource Switchboard</a> and take one of two following options:</p>
<img src="https://subugoe.github.io/factsheets_sshoc_services/images/00switchboardHomepage.png" alt="Image not found" width="75%" height="auto"/>
<h3>1. One of two following options</h3>
<ol>
<li>Either a researcher is already familiar with tools offered and know what is best to use answering research question or</li>
<li>he or she wishes a pre-selection of tools best fitting.</li>
</ol>
<p>If <b>1.</b> researcher can select tools by him- or herself clicking on Tool inventory choosing wished and afterwards finds a three ways function:</p>
<ol>
<li>uploading a file,</li>
<li>submitting an URL or</li>
<li>submitting text.</li>
</ol>
<p>If <b>2.</b> he or she may simple type in <a href="https://switchboard.clarin.eu/input" target="blank">https://switchboard.clarin.eu/input</a> in address bar of a browser and is facing three ways function, mentioned above.</p>
<h2>Which file formats and languages</h2>
<p>By dragging a simple plain text file into field <b>Upload File</b> one can learn which <b>Mediatype</b> (file formats) and <b>Language(s)</b> are excluded from processing in general. Eg. both <i>x-mobipocket-ebook</i> and <i>xhtml+xml</i> are not supported whilst PDF is supported.</p>
<p><b>Mind:</b> That a file format is not excluded completely does not mean that it can be processed with all possible tools thus it is highly recommended converting files into plain text, beforehand, if possible and no critical information will be lost.</p>
<h2>Usage</h2>
<p>In order to use <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a> <a href="https://switchboard.clarin.eu/input" target="_blank"> <i>Upload files or text</i></a> has been clicked on and plain text file of Spanish drama <i>A Dios por razón de estado</i> by Pedro Calderón de la Barca has been dragged onto field <i>Upload File</i>. Selection of four matching tools will be shown, videlicet for dependency parsing <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a>, <i>Voyant Tools</i> for distant reading, for NER <i>NLP-HUB</i> and <i>WebLicht Advanced Mode</i> for text analytics. Different to this following 16 tools are shown after upload of William Shakespeare's <i>Cymbeline</i> as plain text file:</p>
<ol>
<li>For constituency parsing <i>WebLicht Const Parsing</i>,</li>
<li>for dependency parsing three,
<ul>
<li><i>Spacy</i> (hosted by D4Science) - EN</li>
<li><a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a></li>
<li><i>WebLicht Dep Parsing EN</i>,</li>
</ul>
</li>
<li>for distant reading <i>Voyant Tools</i>,</li>
<li>for lemmatization
<ul>
<li><i>CSTLemma</i> (hosted by D4Science) and</li>
<li><i>WebLicht Lemmas EN</i>,</li>
</ul>
</li>
<li>for machine translation <i>LINDAT Translation</i>,</li>
<li>a morpho-syntactic tagger called <i>Tagger NLTK</i>,</li>
<li>for morphological analysis <i>WebLicht Morphology EN</i>,</li>
<li>for Named Entity Recognition three,
<ul>
<li><i>NER NLTK</i></li>
<li><i>NLP-HUB (multiple NER tools)</i></li>
<li><i>WebLicht NamedEntities EN</i>,</li>
</ul>
</li>
<li>a POS tagger named <i>WebLicht POSTags Lemmas EN</i>,</li>
<li>Text Analytics with <i>WebLicht Advanced Mode</i> and</li>
<li>for Text Enhancement <i>Distanbol</i>.</li>
</ol>
<p>By clicking on <i>Open</i> <a href="http://ufal.mff.cuni.cz/udpipe" target="_blank"> <i>UDPipe</i></a> this application starts in a new tab window and spanish model for text processing is offered and processing is starting automatically. By clicking on <i>Advanced Options</i> further adjustments are possible and a new processing by clicking on button <i>Process input</i> is possible. Output both becomes visible in separate frame in tab window and can be downloaded as file in conllu format which is similar to a csv file.</p>
