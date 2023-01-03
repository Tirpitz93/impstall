import logging
from PyInstaller.utils.hooks import collect_data_files
logger = logging.getLogger(__name__)
logging.info(f"Registering hidden pip imports from impstall")

# Get the cacert.pem
datas = collect_data_files('pip')



hiddenimports = [
    "pip",
    "pip._internal.commands.install",
    "pip._vendor.certifi",
        ]

logging.info(f"Hidden imports: {hiddenimports}")
logging.info(f"Registered hidden pip imports from impstall")