# -*- coding: utf-8 -*-
"""
Date     : 2016/07/18 21:48:15
FileName : youdao_dict.py
Author   : septicmk
"""

import urllib, urllib2
import os, sys
import re, time
import logging
import json
import subprocess

def json_encode(j):
    return json.dumps(j, indent=4)
def json_decode(j):
    return json.loads(j)

def query(word):
    if len(word) > 1 and not word[-1].isalpha():
        word = word[0:-1]
    try:
        url = 'http://fanyi.youdao.com/openapi.do?keyfrom=TransMe&key=597592640&type=data&doctype=json&version=1.1&q=' + word
        data = urllib2.urlopen(url).read()
        js = json_decode(data)

        if 'basic' not in js:
            return (None,None,None)

        translation = '<br/>'.join(js['translation'])
        if 'phonetic' in js['basic']:
            phonetic = js['basic']['phonetic']
        else:
            phonetic = ''
        explains = '<br/>'.join(js['basic']['explains'])
        web = '<br/>'.join( ['%s: %s'%(i['key'], ' '.join(i['value'])) for i in js['web'][:3] ] )
        return (translation,explains,web)
    except:
        return (None,None,None)

if __name__ == "__main__":
    print query("test")
