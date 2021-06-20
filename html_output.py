#!/usr/bin/env python3

import json
import os
from datetime import datetime
from jinja2 import Template

template_file = "templates/env_info_html.j2"
data_file = "env_info.json"
html_file = "report.html"
unreach_file = "unreachable.txt"


def main():
    # -- get the template source --
    with open(template_file) as f:
        template_source = f.read()

    # -- get data
    data_json = open(data_file)
    data = json.load(data_json)

    # -- get unreachable data
    if os.path.exists(unreach_file):
        with open(unreach_file) as f:
            unreachables = [line.strip() for line in f]
    else:
        unreachables = []

    template = Template(template_source)
    html = template.render(envs=data,
                           hdr="Environment monitoring",
                           dtutc=datetime.utcnow(),
                           title="Environment monitoring",
                           unreachables=unreachables)
    # -- write out the rendered html
    with open(html_file, "w") as f:
        f.write(html)


if __name__ == '__main__':
    main()
