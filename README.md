# International collaboration for survey


[![DOI](https://zenodo.org/badge/63957124.svg)](https://zenodo.org/badge/latestdoi/63957124)


In 2016 the Software Sustainability Institute ran the first survey of Research Software Engineers (RSEs) - the people who write code in academia. This produced the first insight into the demographics, job satisfaction, and practices of RSEs. To support and broaden this work, the Institute will run the UK survey every year and - it is hoped - will expand the survey so that insight and comparison can be made across different countries. Ultimately, we hope that these results, the anonymised version of which will all be open licensed, will act as a valuable resource to understand and improve the working conditions for RSEs.

In 2017 we also surveyed Canadian RSEs and we added four further countries, Germany, Netherlands, South Africa and USA. 
Our thanks to our partners: Scott Henwood (Canada), Stephan Janosch and Martin Hammitzsch (Germany), Ben van Werkhoven and Tom Bakker (Netherlands), Anelda van der Walt (South Africa) and Daniel Katz and Sandra Gesing (USA).

This repository is used to create and analyse international surveys. It use csv file, limesurvey and jupyter notebook. Each country create a specific csv question file where the questions are stored. Then from this file a limesurvey's file is create and the service is used to collect answers. Once the answers are collected, the analysis are automated and create a jupyter notebook with all the descriptive analysis. For more details please refer to the [HOWTOCONTRIBUTE](https://github.com/softwaresaved/international-survey/blob/master/HOW%20TO%20CONTRIBUTE.md).


## Published results for the 2017 survey

We publish the results under the form of notebooks. All surveys have an attached 'public.csv' file. Theses files have been cleaned of all sensitive data. Therefore, the jupyter notebooks show some results that are not contained in the 'public.csv'.

|Country | Notebook | Dataset |
|  :-:       |  :-:   |  :-:  |
|Canada| 	[Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_can_2017_narrative.ipynb)| [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/can/data/public_data.csv)|
|Germany|  [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_de_2017_narrative.ipynb)| [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/de/data/public_data.csv)|
|Netherlands | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_nl_2017_narrative.ipynb)    | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/nl/data/public_data.csv)|
|South Africa | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_zaf_2017_narrative.ipynb)  	 | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/zaf/data/public_data.csv)|
|UK  | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_uk_2017_narrative.ipynb) | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/uk/data/public_data.csv)|
|USA | [Narrative](https://github.com/softwaresaved/international-survey/blob/master/analysis/results_us_2017_narrative.ipynb)  | [data](https://github.com/softwaresaved/international-survey/blob/master/analysis/2017/us/data/public_data.csv) |


## Contributors
Here is a list of contributors for the 2017 version of the survey (alphabetic order). They are also mentioned in the [.zenodo.json](https://github.com/softwaresaved/international-survey/blob/master/.zenodo.json) to be automatically added to the DOI.

* Stephan Druskat
* Sandra Gesing
* Martin Hammitzsch
* Scott Henwood
* Simon Hettrick
* Stephan Janosch
* Katrin Leinweber
* Olivier Philippe
* Nooriyah P. Lohani
* Nicholas R. May
* Manodeep Sinha
* Daniel S. Katz
* Anelda van der Walt
* Ben van Werkhoven


## Funders
The Software Sustainability Institute is supported by EPSRC grant EP/H043160/1 and EPSRC/ESRC/BBSRC grant EP/N006410/1, with additional project funding from Jisc and NERC. Collaboration between the universities of Edinburgh, Manchester, Oxford and Southampton.
