import os
# import sys
# from datetime import timedelta
# import paramiko
from loguru import logger

from lib import config as conf, strings
import lib.log.logger as logger_lib
from lib import files
from lib import ssh
from lib import cli


@logger.catch
def main():
    # init program
    root_folder = os.getcwd()
    logger_lib.init_logger(strings.__project_name__)
    ca = cli.ConsoleApp()  # console app instance
    _target_station = ca.args.station.lower()
    logger.info(strings.Console.program_start)
    try:
        # get datetime objects
        dates_list, dates_str = files.get_date_object_list(data_range_str=ca.args.date)
        # get datetime file objects
        files_targets = files.get_date_export_path_list(date_objects=dates_list,
                                                        target_path=conf.stations[_target_station]['target_folder'],
                                                        station=_target_station,
                                                        file_name_format=conf.main['remote_file_name_format']
                                                        )
        # info: prepared vars to download
        logger.info(strings.Console.info_prepare_download_info.format(station=_target_station,
                                                                      dates=dates_str,
                                                                      days=len(dates_list)
                                                                      ))
        # download files
        ssh.dowloader(server_ip=conf.stations[_target_station]['ip'],
                      s_login=conf.stations[_target_station]['login'],
                      s_pass=conf.stations[_target_station]['pass'],
                      target_list=files_targets,
                      out_path=root_folder,
                      logger=logger)

        # prepare string of file names
        file_names = files.get_file_names_list_as_str(targets=files_targets)
        # success: report of finished
        logger.success(strings.Console.success_download_files.format(files=file_names))

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
