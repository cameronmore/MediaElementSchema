# Documentation

## Background
The Meda Element Schema was created out of the need to (1) automatically convert bibliographic citations into multiple formats (2) in a lightweight package. Although great tools like Zotero exist, something more minimal was desired.

The schema itself was developed initially as a way to represent the input to a function which generated the citation. Roderic Page has documented several competing representations of bibliographic entries in JSON [here](https://github.com/rdmpage/bibliographic-metadata-json?tab=readme-ov-file), which include BibJSON, CLS-JSON, and JSON-LD. At first, BibJSON seemed promising, but some of the keys seemed unintuative--and more importantly, the project is inactive. Moreover, many of these options did not preserve the ability to clearly distinguish author one and author two, or the components of an author's name (which are written differnetly depending on the media type and citation style). The other options had more drawbacks--a JSON-LD implementation seemed interesting, but having to deal with nested JSON-LD for no obvious benefit steered me away from that option.

Instead, I crafted my own schema.

## The Schema


## Media Element Schema Ecosystem
Although important, the schema is noting without tools and scripts that can manipulate data with it. To that end, on this repository are two scripts that perform the originally intended function of generating well-formed citations in multiple formats and validating JSON instances of the schema.

Eventually, there should be a method to convert this schema into BibTeX, RIS, and the RDF that Zotero uses. There should also be a (web based) UI for translating the raw input into the multiple formats (though dozens of those do already exist, so why make another?).