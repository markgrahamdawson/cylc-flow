#!/usr/bin/python

#         __________________________
#         |____C_O_P_Y_R_I_G_H_T___|
#         |                        |
#         |  (c) NIWA, 2008-2010   |
#         | Contact: Hilary Oliver |
#         |  h.oliver@niwa.co.nz   |
#         |    +64-4-386 0461      |
#         |________________________|


# o SYSTEM CONFIG MODULE FOR THE CYLC SYSTEM DEFINITION DIRECTORY:
#  /home/oliverh/cylc/sys/examples/file-move
# o REFER TO THE CYLC USER GUIDE FOR DOCUMENTATION OF CONFIG ITEMS. 
# o THIS FILE WAS AUTOGENERATED BY 'cylc configure' BUT WILL NOT
# BE OVERWRITTEN ON RECONFIGURATION UNLESS YOU FORCE IT. 

# Configured items are held in a dict (Python associative array): 
#   items[ 'item' ] = value.
# Note that some "values" are themselves lists or dicts.

from config import config
from task_list import task_list
from system_info import info
import logging  # for logging level
import os       # os.environ['HOME']

class system_config( config ):

    def __init__( self, sysname ):
        config.__init__( self, sysname )

        # system title
        self.items[ 'system_title' ] = 'FILE-MOVE EXAMPLE SYSTEM'
        
        # system info
        self.items['system_info']['info'] = info   # SEE system_info.py
        # add more descriptive information as you like, e.g.:
        # self.items[ 'system_info' ]['colours'] = 'red, blue, green'

        # list of legal startup hours, if this system is so restricted
        # e.g.: self.items['legal_startup_hours'] = [ 6 ]
        # or:   self.items['legal_startup_hours'] = [ 6, 18 ]

        # task list
        self.items['task_list'] = task_list     # SEE task_list.py

        # task insertion groups, e.g:
        # self.items['task_groups']['foo'] = ['bar', 'baz']

        # default job submit method, e.g.:
        # self.items['job_submit_method'] = 'background2'

        # environment variables available to all tasks

        # 1/ $TMPDIR, used for all input and output files
        user = os.environ['USER'] 
        self.items['environment']['TMPDIR'] = '/tmp/' + user + '/' + sysname

        # 2/ $REAL_TIME_ACCEL, used to scale real run times for fast operation 
        self.items['environment']['REAL_TIME_ACCEL'] = 360

        #self.items['logging_level'] = logging.DEBUG
# END OF FILE
