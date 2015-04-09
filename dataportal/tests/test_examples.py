from nose.tools import assert_true
from ..examples.sample_data import (temperature_ramp, multisource_event,
                                    image_and_scalar, step_scan)
from metadatastore.api import Document
from filestore.utils.testing import fs_setup, fs_teardown
from metadatastore.utils.testing import mds_setup, mds_teardown

examples = [temperature_ramp, multisource_event, image_and_scalar, step_scan]

def setup():
    fs_setup()
    mds_setup()


def teardown():
    fs_teardown()
    mds_teardown()


def run_example_programmatically(example):
    events = example.run()
    assert_true(isinstance(events, list))
    assert_true(isinstance(events[0], Document))


def test_examples_programmatically():
    for example in examples:
        yield run_example_programmatically, example
