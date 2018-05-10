# -*- coding: utf-8 -*-

"""
test_cyme_to_ephasor
----------------------------------

Tests for Cyme --> Ephasor conversion
"""
import os
import six

if six.PY2:
    from backports import tempfile
else:
    import tempfile

import pytest as pt

current_directory = os.path.realpath(os.path.dirname(__file__))

def test_cyme_to_ephasor(output_folder=None,input_folder=None):
    '''
        Test the Cyme to Ephasor conversion.
    '''
    from ditto.store import Store
    from ditto.readers.cyme.read import Reader
    from ditto.writers.ephasor.write import Writer

    cyme_models=[f for f in os.listdir(os.path.join(current_directory, 'data/small_cases/cyme/')) if not f.startswith('.')]
    if input_folder == None:
        for model in cyme_models:
            m = Store()
            r = Reader(data_folder_path=os.path.join(current_directory, 'data/small_cases/cyme',model))
            r.parse(m)
            #TODO: Log properly
            print('>Cyme model {model} read...'.format(model=model))
            if output_folder is None:
                t = tempfile.TemporaryDirectory()
                w = Writer(output_path=t.name)
                w.write(m)
            else:
                w = Writer(output_path=output_folder,output_name=model)
                w.write(m)
            #TODO: Log properly
            print('>...and written to Ephasor.\n')
    else:
        m = Store()
        r = Reader(data_folder_path=input_folder)
        r.parse(m)
        #TODO: Log properly
        print('>Cyme model {model} read...'.format(model=model))
        if output_folder is None:
            t = tempfile.TemporaryDirectory()
            w = Writer(output_path=t.name)
            w.write(m)
        else:
            w = Writer(output_path=output_folder)
            w.write(m)
        #TODO: Log properly
        print('>...and written to Ephasor.\n')



if __name__ == '__main__':
    test_cyme_to_ephasor(output_folder = os.path.join(current_directory,'results','cyme_to_ephasor'))
