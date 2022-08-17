__project_name__ = 'SyncLoader'
__program_version__ = 1.0


class Console:
    program_start = f'Program {__project_name__} v.{__program_version__} started. '
    format_date_range = '{date_from} - {date_to}'
    info_prepare_download_info = 'Selected station <{station}>, range: {dates} ({days} days)..'
    info_download_file_progress = 'Downloading file <{file}> in progress..'
    success_download_files = 'File download: <{files}> completed!'

    exception_invalid_date_string_format = 'Invalid input date string format, skipping..'


class Report:
    mail_subject = '{project_name}: Error report'.format(project_name=__project_name__)
