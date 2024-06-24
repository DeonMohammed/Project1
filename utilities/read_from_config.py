from configparser import ConfigParser


def readconfig(category, key):
    config = ConfigParser()
    config.read('D:\Python Projects\SeleniumHybridFramework\Config\config.ini')
    return config.get(category, key)

# from configparser import ConfigParser, NoSectionError, NoOptionError


# def readconfig(category, key):
#     config = ConfigParser()
#     config.read('Config/config.ini')
#
#     try:
#         return config.get(category, key)
#     except NoSectionError:
#         raise ValueError(f"Section '{category}' not found in the config file.")
#     except NoOptionError:
#         raise ValueError(f"Key '{key}' not found in section '{category}'.")
#
#
