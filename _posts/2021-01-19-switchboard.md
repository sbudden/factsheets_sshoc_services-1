---
layout:     default
title:      switchboard
date:       2021-01-19 11:55
---

# Switchboard

The following text is used with kind permission by the [TextGrid Repository](https://gitlab.gwdg.de/dariah-de/textgridrep-portal/-/blob/develop/docs/switchboard.en.md). For this reason the following tutorial is written from the perspective of an user visiting the TextGrid Repository and initialising the Switchboard from there.

The integration of the [Language Resource Switchboard](https://switchboard.clarin.eu/) into the TextGrid Repository (TextGridRep) is an important step in the course of the merging of digital research data infrastructures within the humanities and social sciences ([CLARIAH](https://www.clariah.de/) and [SSHOC](https://www.sshopencloud.eu/)).
The corpora offered in the TextGridRep are primarily relevant for literary studies or for computer philology in general.
For many analyses in these fields, tools from the field of Natural Language Processing and linguistic annotation are important in the context of corpus creation and corpus preparation. The Switchboard offers a wide range of such tools.

Through the direct integration of the Switchboard, we enable texts to be automatically analyzed and annotated for linguistic features in a convenient way using various tools.
The Switchboard works with web applications; thus, downloads and installations are not necessary and the tools access external servers, which means that users do not require large computing capacities.
The step of downloading texts from the TextGridRep and then uploading them back to the Switchboard is eliminated in this way.


## Starting the Switchboard

To start the program, open a text and click "Switchboard" on the left side of your screen (by clicking the blue 🛈, you will get to this documentation):

![Link to the Switchboard](images/Switchboard_en_Bild1.png)

You will then be redirected to the Switchboard page.
<!---Wie Sie sehen, gibt es zwei Möglichkeiten: "Switchboard (TEI)" und "Switchboard (txt)". Wählen Sie bitte entsprechend der Entscheidung, auf Grundlage welchen Dateiformats Sie eine Analyse vornehmen möchten. Das TEI-Format bietet im Üblichen eine größere Bandbreite verschiedener Auswertungsmöglichkeiten, allerdings kann es aktuell noch von wenigen Tools innerhalb des Switchboards verarbeitet werden. Außerdem sind zwar die meisten Texte im TextGridRep TEI-kodiert, jedoch noch nicht alle. Um auf möglichst viele verschiedene Tools zugreifen zu können, wählen Sie bitte das txt-Format.
Haben Sie sich für eine Variante des Switchboards entschieden, wechselt der Bildschirm zur Switchboard-Seite.-->

![Document and tool overview](images/Switchboard_en_Bild2a.png)

In the upper part of your screen (arrow 1) you will now see your input resource, i.e. the text you want to analyze.
The media format is listed next to it.
To the right, you will see the language which is assigned automatically.
You usually do not need to make any changes in this area.
However, please check if the Switchboard has automatically selected the correct file format and language and correct them if necessary.
The Switchboard automatically offers a selection of tools that can work with the entered file format and the language of the text.
As a result, you will see (arrows 2) various tools and services that can perform automatic analyses and annotations (e.g. Constituency Parsing, Dependency Parsing, etc.) of the selected text.


## Using tools

![Using tools and documentations of them](images/Switchboard_en_Bild2b.png)

To apply a tool to your selected text, click on the green "Start Tool" button (arrow 3).
You will then be redirected to the website of the tool that has already loaded your text and prepared it for processing.
Sometimes the processing starts automatically, sometimes you have to start it by yourself.
If you wish documentation of the tools, please click on the blue symbol next to the tool name (arrow 4).


## Applying the Switchboard to your collections

Up to now, the Switchboard can only process one text at a time – however, the demand can be announced according to the [Switchboard-FAQ-list](https://switchboard.clarin.eu/help).
Therefore you unfortunately do not have the possibility – as in [Voyant](https://textgridrep.org/docs/voyant?lang=en) – to apply the Switchboard to your self-created collection in your [shelf](https://textgridrep.org/docs/shelf?lang=en).


## References

- [About the Language Ressource Switchboard](https://switchboard.clarin.eu/about)
- Claus Zinn, [The Language Resource Switchboard](https://www.mitpressjournals.org/doi/full/10.1162/coli_a_00329). Computational Linguistics 44(4), pages 631-639, December 2018.
- Claus Zinn. [A Bridge from EUDAT's B2DROP cloud service to CLARIN's Language Resource Switchboard](https://ep.liu.se/ecp/147/004/ecp17147004.pdf). Selected papers from the CLARIN Annual Conference 2017, Budapest, 18-20 September 2017, Linköping University Electronic Press vol. 147, pages 36-45, 2018.
- Claus Zinn. [The CLARIN Language Resource Switchboard](https://www.clarin.eu/sites/default/files/zinn-CLARIN2016_paper_26.pdf). CLARIN 2016 Annual Conference, Aix-en-Provence, France, 2016.
- Claus Zinn, Marie Hinrichs, Emanuel Dima, Dieter van Uytvanck. [The Switchboard specification](https://office.clarin.eu/v/CE-2015-0684-LR_switchboard_spec.pdf) (Milestone 2.2 of the CLARIN-PLUS project).
- Claus Zinn. [D2.5 LR Switchboard (software)](https://office.clarin.eu/v/CE-2016-0881-CLARINPLUS-D2_5.pdf). Deliverable in the CLARIN-PLUS project.


## Further documentation and tutorials

Further help can be found at the [Switchboard help page](https://switchboard.clarin.eu/help) as well as at the documentations of the different tools.
An overview of all services and tools offered by the Switchboard can be found [here](https://switchboard.clarin.eu/tools).


## Contact

Do you have further questions concerning the Switchboard in TextGrid?
Please [contact](https://textgrid.de/en/kontakt/) us!
If you have questions about individual tools provided in the Switchboard, please first consult their documentation and feel free to contact their respective developers.

## Attribution

This Switchboard tutorial has been authored by the colleagues at TextGrid, most notably Lukas Weimer.
