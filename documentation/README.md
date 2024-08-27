# Documentation

## Background
The Meda Element Schema was created out of the need to (1) automatically convert bibliographic citations into multiple formats (2) in a lightweight package. Although great tools like Zotero exist, something more minimal was desired.

The schema itself was developed initially as a way to represent the input to a function which generated the citation. Roderic Page has documented several competing representations of bibliographic entries in JSON [here](https://github.com/rdmpage/bibliographic-metadata-json?tab=readme-ov-file), which include BibJSON, CLS-JSON, and JSON-LD.

At first, BibJSON seemed promising, but some of the keys seemed unintuative--and more importantly, the project is inactive. Many of these options did not preserve the ability to clearly distinguish author one and author two, or the components of an author's name (which are written differnetly depending on the media type and citation style), and combined data that I thought should be kept separately (like first and last page numbers for a piece of text).

A JSON-LD implementation seemed interesting at first, but having to deal with nested JSON-LD for no obvious, immediate benefit steered me away from that option.

Instead, I crafted my own schema.

## The Schema and Script
To use the script in`scripts/Converter.py`:
```python
import json

SerializeFromJSON("YOUR_JSON.json","MLA")
```
This will read a JSON file looking for the "mediaData" as the main key of `YOUR_JSON.json` and print the results. There is other _planned_ functionality for the script that is described in the function notes, but it does not work. (For example, it does not properly italicize anything).

The schema itself is written in [JSON Schema](https://json-schema.org/) and heavily inspired by BibJSON, RIS, and BibTeX, with keys for publisher information, authors, editors, translators, and the length of a piece of media (time in video/audio media, page numbers in print).


## Media Element Schema Ecosystem
Although important, the schema is noting without tools and scripts that can manipulate data with it. To that end, on this repository are two scripts that perform the originally intended function of generating well-formed citations in multiple formats and validating JSON instances of the schema.

Eventually, there should be a method to convert this schema into BibTeX, RIS, and the RDF that Zotero uses. There should also be a (web based) UI for translating the raw input into the multiple formats (though dozens of those do already exist, so why make another?).