import os
import sys
sys.path.append('../tracer/')
import tracer

import logging
l = logging.getLogger("tracer.tests.test_tracer")

bin_location = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../binaries/'))
fnf_bin_location =  '../examples/targets' # location relative to FrogAndFuzz -> redis name


logging.getLogger("tracer").setLevel("DEBUG")
logging.getLogger("redis_com").setLevel("DEBUG")

def test_me():
    '''
    Test
    '''

    # test a valid palindrome
    t = tracer.Tracer(os.path.join(fnf_bin_location, "testme"), os.path.join(bin_location, "testme"), "racecar\n")
    result_path, crash_state = t.run()

    result_state = result_path.state

    # make sure angr modeled the correct output
    stdout_dump = result_state.posix.dumps(1)
    print(stdout_dump)




if __name__ == "__main__":

    test_me()
