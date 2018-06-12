# -*- coding: utf-8 -*-
"""
test_gridlabd_to_ephasor
----------------------------------

Tests for GridlabD --> Ephasor conversion
"""
import six

if six.PY2:
    from backports import tempfile
else:
    import tempfile

import pytest as pt
import os

current_directory = os.path.realpath(os.path.dirname(__file__))

@pt.mark.skip() #currently not running...
def test_gridlabd_to_ephasor(output_folder=None,input_file_loc=None):
    from ditto.readers.gridlabd.read import Reader
    from ditto.store import Store
    from ditto.writers.ephasor.write import Writer

    gridlabd_models=[f for f in os.listdir(os.path.join(current_directory,'data/small_cases/gridlabd/')) if not f.startswith('.')]
    if input_file_loc is None:
        for model in gridlabd_models:
            m = Store()
            r = Reader(input_file=os.path.join('data','small_cases','gridlabd',model))
            r.parse(m)
            m.set_names()
            #TODO: Log properly
            print('>Gridlab-D model {model} read...'.format(model=model))
            if output_folder is None:
                t = tempfile.TemporaryDirectory()
                w = Writer(output_path=t.name)
                w.write(m)
            else:
                w = Writer(output_path=output_folder,output_name=model)
                w.write(m)
            print('>...and written to Ephasor.\n')

    else:
        m = Store()
        r = Reader(input_file=input_file_loc)
        r.parse(m)
        m.set_names()
        print('>Gridlab-D model {model} read...'.format(model=input_file_loc))
        if output_folder is None:
            t = tempfile.TemporaryDirectory()
            w = Writer(output_path=t.name)
            w.write(m)
        else:
            w = Writer(output_path=output_folder,output_name='output')
            w.write(m)
        print('>...and written to Ephasor.\n')

if __name__ == '__main__':
    test_gridlabd_to_ephasor(output_folder = os.path.join(current_directory,'results','gridlabd_to_ephasor'))
#test_gridlabd_to_ephasor(output_folder = os.path.join(current_directory,'results','rtca'),input_file_loc=os.path.join(current_directory,'data','big_cases','gridlabd','rtca','model_raw.glm'))
