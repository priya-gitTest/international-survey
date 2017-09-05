#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Olivier Philippe'


"""
Limesurvey offers the possibility to import/export a TSV file containing all the information
of the survey structure. Using this possibility, this script aims to translate the files used
by the different groups to creates their survey, into a compatible TSV file.
It take only the argument of the folder where all the information is stored, and create a new
compatible file.
All information about the TSV file structure can be retrieved here:
    https://manual.limesurvey.org/Tab_Separated_Value_survey_structure
"""

import csv
import sys
import os
from collections import OrderedDict
from include.logger import logger
from config.config import creationConfig as main_config
import importlib


RUNNING = 'dev'

if RUNNING == 'dev':
    DEBUGGING='DEBUG'
elif RUNNING == 'prod':
    DEBUGGING='INFO'

logger = logger(name='creating survey', stream_level=DEBUGGING)


def import_config(folder):
    """
    Import the config file associated with the folder name
    """
    module = 'config.{}'.format(folder)
    return importlib.import_module(module).config()


def create_empty_row():
    """
    Create an Ordered dictionary to be used to translate csv file to tsv
    """
    return OrderedDict((k, '') for k in main_config.main_headers)


def init_outfile(folder):
    """
    Rewrite over the existing file to avoid issue of appending and
    return the path to the file
    """
    outfile_name = folder + '_to_import.txt'
    outfile = os.path.join(folder, outfile_name)
    with open(outfile, 'w') as f:
        w = csv.DictWriter(f, delimiter='\t',
                           lineterminator='\n',
                           quotechar='"',
                           fieldnames=main_config.main_headers)
        w.writeheader()
    return outfile


def read_survey_file(folder):
    """
    Read the survey csv file and yield each line as a dictionary
    """
    question_file = os.path.join(folder, '.'.join([folder, 'csv']))
    with open(question_file, 'r') as f:
        csv_f = csv.reader(f, delimiter=';', quotechar='"')
        for row in csv_f:
            yield row


def write_row_outfile(outfile, row):
    """
    """
    with open(outfile, 'a') as f:
        w = csv.DictWriter(f, delimiter='\t',
                           lineterminator='\n',
                           quotechar='"',
                           fieldnames=main_config.main_headers)
        w.writerow(row)
        # f.write({k: row[k] for k in row})

def to_modify(original_list, modified_list):
    """
    """
    return_list = list()
    for element in original_list:
        replaced = False
        for e in modified_list:
            if element['text'] == e['text']:
                return_list.append(e)
                replaced = True
                break
        if replaced is False:
            return_list.append(element)
    return return_list


def to_add(original_list, list_to_add):
    """
    """
    for obj in list_to_add:
        original_list.insert(obj[1], obj[0])
    return original_list


def create_header(main_config, specific_config):
    """
    """
    good_parameters = to_modify(main_config.global_headers, specific_config.header_to_modify)
    good_parameters = to_add(main_config.global_headers, specific_config.header_to_add)
    return good_parameters


def add_from_list(outfile, list_to_copy):
    """
    """
    for element in list_to_copy:
        row = create_empty_row()
        row.update(element)
        write_row_outfile(outfile, row)


def main():
    # Get which survey
    folder = sys.argv[1]

    # Import specific config file
    specific_config = import_config(folder)
    print(specific_config.header_to_modify)

    # Init an empty survey file
    outfile = init_outfile(folder)

    # Create a copy the header to the empty file
    config_header = create_header(main_config, specific_config)

    # Record the copy into the file
    add_from_list(outfile, config_header)

    # Get the additional languages
    add_lang = specific_config.additional_language

    # Get the welcome message

    # Get the end message

    # Create the description

    # Copy the description to the header

    # Open the survey file

    # For each row

    # Check the group

    # If group is new -- create the group in the file

    # Check the question

    # Create the type of question

    # Check for condition

    # Check for type of answer

    # Check for the answer file

    # Do everything for the new language


if __name__ == "__main__":
    main()
