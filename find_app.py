import os
from shutil import which

def find_app(app: str) -> str:
    """
    Search File System for an instance of the app name specified
    """

    app_loc = which(app)

    if app_loc is None:
        break_main = False

        for root, dirs, files in os.walk('/'):
            del dirs

            for name in files:
                # if the file matches the app name, add full path and break loop
                if name == app:
                    break_main = True
                    app_loc = os.path.join(root, name)

                    break

            if break_main is True:
                break

    if app_loc is None:
        raise FileNotFoundError(f'App {app} not found in File System! Check that app exists and permissions to the app are correct')