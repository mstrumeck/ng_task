import re


def camel_case_split(identifier):
    matches = re.finditer(
        ".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)", identifier
    )
    return "_".join([m.group(0) for m in matches]).lower()
