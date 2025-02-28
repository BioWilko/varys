import logging
from collections import namedtuple
import sys
import json
import os


varys_message = namedtuple("varys_message", "basic_deliver properties body")


class configurator:
    def __init__(self, profile, config_path):
        try:
            with open(config_path, "rt") as config_fh:
                config_obj = json.load(config_fh)
        except:
            print(
                "Configuration JSON does not appear to be valid or does not exist",
                file=sys.stderr,
            )
            sys.exit(11)

        if config_obj["version"] != "0.1":
            print(
                "Version number in the ROZ configuration file does not appear to be current, ensure configuration format is correct if you experience errors",
                file=sys.stderr,
            )

        profile_dict = config_obj["profiles"].get(profile)
        if profile_dict:
            try:
                self.profile = profile
                self.username = str(profile_dict["username"])
                self.password = str(profile_dict["password"])
                self.ampq_url = str(profile_dict["amqp_url"])
                self.port = int(profile_dict["port"])
            except KeyError:
                print(
                    f"Varys configuration JSON does not appear to contain the necessary fields for profile: {profile}",
                    file=sys.stderr,
                )
                sys.exit(11)
        else:
            print(
                f"Varys configuration JSON does not appear to contain the specified profile {profile}",
                file=sys.stderr,
            )
            sys.exit(2)
