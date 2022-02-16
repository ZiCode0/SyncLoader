import os
import paramiko

from lib import strings


def printTotals(transferred, toBeTransferred):
    print(f"Transferred: {transferred}\tOut of: {toBeTransferred}")


def dowloader(server_ip, s_login, s_pass: str, target_list: list, out_path='.', logger=None):
    """
    Download files from ssh server
    :param server_ip:
    :param s_login:
    :param s_pass:
    :param target_list:
    :param out_path:
    :param logger: logger instance for debug
    :return:
    """
    # init connection
    ssh = paramiko.SSHClient()
    # # skip key policy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # # connect
    ssh.connect(server_ip, username=s_login, password=s_pass)
    # # make sftp instance
    sftp = ssh.open_sftp()
    # download each file
    for path in target_list:
        # prepare out path
        _file_name = os.path.basename(path)
        _out_path_file = os.path.join(out_path, _file_name)
        if logger:
            logger.info(strings.Console.info_download_file_progress.format(file=_file_name))
        # download file
        sftp.get(path, _out_path_file)

    # close connection
    sftp.close()
    ssh.close()
