#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
from sdmdata.worker_daemon import Daemon
from web_server import app


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
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
        # self.delpid()
        sys.exit(0)
        # self.logger.debug("end sleep")


if __name__ == "__main__":
    pathname = os.path.dirname(sys.argv[0])
    work_path = os.path.abspath(pathname)
    print work_path
    daemon = MyDaemon(work_path, "web_server")
    daemon.handle_argument()



