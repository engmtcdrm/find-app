'''
FindApp is a class that searches the File System for an app and returns the path to the app.
'''
import os
from typing import Optional, Type, Any, cast, Union
from shutil import which
import subprocess
from pathlib import Path

class FindApp:
    """
    FindApp is a class that searches the File System for an app and returns the path to the app.

    :param path_type: The type of path to return. If None, returns str. If os.PathLike[str],
        returns os.PathLike[str].
    """

    def __init__(self, path_type: Optional[Type[Any]] = None):
        self.type = path_type

        self.locate_apps = [
            'mlocate',
            'plocate',
            'locate'
        ]

    def _fix_app_result(self, app_path: Union[str, os.PathLike[str]]) -> Union[str, os.PathLike[str]]:
        """
        Fixes the result of the app search.

        :param app_path: The app_path to fix.
        """
        if self.type is not None and not isinstance(app_path, self.type):
            if self.type is str:
                return os.fsdecode(app_path)
            else:
                return cast("os.PathLike[str]", self.type(app_path))

        return app_path

    def find(self, app: str) -> str:
        """
        Searches the File System for an app and returns the path to the app.

        :param app: The name of the app to search for.

        :returns The path to the app.
        """

        # Attempt to find app via PATH environment variable
        app_loc = which(app)

        # If app found, check if app is executable
        if app_loc is None:
            # Iterate through locate apps trying to find one that is available
            for locate_app in self.locate_apps:
                loc_app = which(locate_app)

                if loc_app is not None:
                    find_sp = subprocess.Popen(f'{loc_app} {app}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    rc = find_sp.wait()

                    found, err = find_sp.communicate()

                    found_list = found.split('\n')

                    # If app found, grab first result and break loop
                    if len(found_list) > 0:
                        app_loc = found_list[0]
                        break

        # If not found, brute force by searching file system
        if app_loc is None or app_loc == '':
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

        return self._fix_app_result(r_app_loc)
