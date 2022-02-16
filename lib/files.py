import os
from datetime import timedelta
import dateutil.parser as dparser

from lib import strings


def get_date_object_list(data_range_str: str) -> tuple:
    """
    Form datetime object list of target days according to range in string format
    :param data_range_str: target date range with divider. Example: 2022.02.02-2022.03.02
    :return:
    """
    _date_divider = '-'
    _date_range = data_range_str.split(_date_divider)
    _export_date_format = '%Y.%m.%d'
    # single date
    if len(_date_range) == 1:
        result_date_list = [dparser.parse(_date_range[0])]
        # prepare export string
        result_date_str = result_date_list[0].strftime(_export_date_format)
    # range(from - to) format
    elif len(_date_range) == 2:
        _date_from, _date_to = [dparser.parse(i) for i in _date_range]
        _delta_days_count = (_date_to - _date_from).days
        result_date_list = [_date_from + timedelta(days=day_num)
                            for day_num in range(_delta_days_count+1)]
        # prepare export string parts
        _date_from_str = result_date_list[0].strftime(_export_date_format)
        _date_to_str = result_date_list[-1].strftime(_export_date_format)
        # prepare export string
        result_date_str = strings.Console.format_date_range.format(date_from=_date_from_str,
                                                                   date_to=_date_to_str)
        # f'{_date_from_str} - {_date_to_str}'
    else:
        raise Exception(strings.Console.exception_invalid_date_string_format)
    return result_date_list, result_date_str


def get_date_export_path_list(date_objects: list, target_path: str,
                              station: str, file_name_format: str) -> list:
    """
    Get target date files to export for remote server
    :param date_objects: datetime object list
    :param target_path: remote server path to source date files
    :param station: target station
    :param file_name_format: format for target file name on server
    :return:
    """
    station_name = station.upper()
    result_path_list = []
    for date_obj in date_objects:

        _file_name = file_name_format.format(station=station_name,
                                             year=str(date_obj.year).zfill(4),
                                             month=str(date_obj.month).zfill(2),
                                             day=str(date_obj.day).zfill(2)
                                             )
        _file_path = os.path.join(target_path, _file_name)
        result_path_list.append(_file_path)
        # print()
    return result_path_list


def get_file_names_list_as_str(targets):
    """
    Return list of targets file names
    :param targets: target paths of files
    :return: list of file names
    """
    name_list = [os.path.basename(path) for path in targets]
    return ', '.join(name_list)
