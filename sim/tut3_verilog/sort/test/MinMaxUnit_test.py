from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from ..MinMaxUnit import MinMaxUnit

def test_1( cmdline_opts ):
  run_test_vector_sim( MinMaxUnit(8), [
    ('in0   in1   out_min*  out_max*'),
    #("in0",   "in1",   "out_min*",  "out_max*"),
    [ 0x00, 0x01, 0x00, 0x01 ],
  ], cmdline_opts )

