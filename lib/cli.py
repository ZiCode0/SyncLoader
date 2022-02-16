import argparse

from lib import strings


class ConsoleApp:
    def __init__(self):
        """
        Initial console app function
        """
        self.app_name = strings.__project_name__
        self.app_version = strings.__program_version__
        self.author = 'ZiCode0'
        self.contacts = '[Telegram] @MrFantomz'
        self.args = None

        # define program description
        text = '{app_name} by {author} v.{app_version}\nContacts: {contacts}'.format(app_name=self.app_name,
                                                                                     author=self.author,
                                                                                     app_version=self.app_version,
                                                                                     contacts=self.contacts)
        # initiate the parser with a description
        parser = argparse.ArgumentParser(description=text)
        # optional params
        parser.add_argument("-v", "--version", help="show program version", action="store_true")
        parser.add_argument("-o", "--out", help="specify absolute/relative out path of result files.")
        # required params
        required_params = parser.add_argument_group('required named arguments')
        required_params.add_argument("-s", "--station", help="specify target station. Ex: PET",
                                     required=True)
        required_params.add_argument("-d", "--date", help="specify target dates to download. Ex: 2022.02.10-2022.02.14",
                                     required=True)

        # parser.add_argument("-c", '--config', help="select config file", default="default")
        self.args = parser.parse_args()
        if self.args.version:
            print(self.app_version)
            quit(0)
