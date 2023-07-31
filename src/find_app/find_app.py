'''
FindApp is a class that searches the File System for an app and returns the full path to the app.
'''
import os
from typing import Optional, Type, Any, cast, Union
from shutil import which
import subprocess
from pathlib import Path
import click

click.Path()

class FindApp:
    """
    FindApp is a class that searches the File System for an app and returns the full path to the app.
    """

    def __init__(self, path_type: Optional[Type[Any]] = None):
        self.type = path_type

    def fix_app_result(self, value: Union[str, os.PathLike[str]]) -> Union[str, bytes, os.PathLike[str]]:
        if self.type is not None and not isinstance(value, self.type):
            if self.type is str:
                return os.fsdecode(value)
            elif self.type is bytes:
                return os.fsencode(value)
            else:
                return cast("os.PathLike[str]", self.type(value))

        return value

    def find(self, app: str) -> str:
        """
        Searches the File System for an app and returns the full path to the app.

        :param app: The name of the app to search for.
/
        returns: The full path to the app.
        """

        # Attempt to find app via PATH environment variable
        app_loc = which(app)

        loc_app = which('locate')

        # If app found, check if app is executable
        if app_loc is not None:
            print('found in PATH')
            pass
        # If app not found, attempt to find app via locate command
        elif loc_app is not None:
            find_sp = subprocess.Popen(f'{loc_app} {app}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            rc = find_sp.wait()

            out, err = find_sp.communicate()

            d = out.split('\n')
        # If app not found, attempt to find app via find command
        else:
            # If not found, brute force by searching file system
            if app_loc is None:
                break_main = False

                # Iterate through file system
                for root, dirs, files in os.walk(os.path.abspath(os.sep)):
                    del dirs

                    # Iterate through files in current directory
                    for name in files:
                        # If the file matches the app name, add full path and break loop
                        if name == app:
                            break_main = True
                            app_loc = os.path.join(root, name)

                            break

                    # If app found, break loop
                    if break_main is True:
                        break

        # If app not found, raise FileNotFoundError
        if app_loc is None:
            raise FileNotFoundError(f'App {app} not found in File System. Check that app exists and permissions to the app are correct.')
        # If app found, but not executable, raise PermissionError
        elif os.access(app_loc, os.X_OK) == False:
            raise PermissionError(f'App {app} does not have the appropriate permissions to be executed.')

        r_app_loc = os.fsdecode(Path(app_loc).resolve())

        return self.fix_app_result(r_app_loc)

    def _validateApp():
        pass
