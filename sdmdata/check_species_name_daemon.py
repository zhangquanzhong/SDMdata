#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
from sdmdata.worker_daemon import Daemon
from sdmdata.check_species_main import check_species_data


class MyDaemon(Daemon):
    def __init__(self, work_path, daemon_name):
        Daemon.__init__(self, pidfile=os.path.join(work_path, daemon_name + "_daemon.pid"),
                        stderr=os.path.join(work_path, daemon_name + '_daemon_err.log'),
                        stdout=os.path.join(work_path, daemon_name + '_daemon_out.log'),
                        stdin='/dev/null')
        # task_mgr_log = time.strftime('%Y%m%d') + '.log'
        # self.logger = mod_logger.logger(task_mgr_log)

    def _run(self):
        # self.logger.debug("begin sleep")
        check_species_data()
        self.delpid()
        sys.exit(0)
        # self.logger.debug("end sleep")


if __name__ == "__main__":
    pathname = os.path.dirname(sys.argv[0])
    work_path = os.path.abspath(pathname)
    daemon = MyDaemon(work_path, "check_species_name_daemon")
    daemon.handle_argument()