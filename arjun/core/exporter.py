import json
import requests

import arjun.core.config as mem
from arjun.core.utils import populate

from arjun.core.utils import create_query_string


def json_export(result):
    """
    exports result to a file in JSON format
    """
    with open(mem.var['json_file'], 'w+', encoding='utf8') as json_output:
        json.dump(result, json_output, sort_keys=True, indent=4)


def text_export(result):
    """
    exports results to a text file, one url per line
    """
    with open(mem.var['text_file'], 'a+', encoding='utf8') as text_file:
        for url, data in result.items():
            clean_url = url.lstrip('/')
            if data['method'] == 'JSON':
                text_file.write(clean_url + '\t' + json.dumps(populate(data['params'])) + '\n')
            else:
                query_string = create_query_string(data['params'])
                if '?' in clean_url:
                    query_string = query_string.replace('?', '&', 1)
                if data['method'] == 'GET':
                    text_file.write(clean_url + query_string + '\n')
                elif data['method'] == 'POST':
                    text_file.write(clean_url + '\t' + query_string + '\n')


def exporter(result):
    """
    main exporter function that calls other export functions
    """
    if mem.var['json_file']:
        json_export(result)
    if mem.var['text_file']:
        text_export(result)
