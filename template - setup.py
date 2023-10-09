#!/usr/bin/env python3
from os.path import join, abspath, dirname, exists
from setuptools import setup
from enum import Enum

"""Шаблон для плагина setup.py.
Представленные константы заполняются информацией, релевантной для плагина.
"""


class PluginType(Enum):
    WAKE_WORD = "wake_word"
    TTS = "tts"
    STT = "stt"
    AUDIO = "audioservice"


PLUGIN_TYPE: PluginType = ""  # один из типов PluginType
PLUGIN_MODULE_NAME = ""  # Alena configuration module name for plugin
PLUGIN_TARGET = ""  # class to use, ex. alena_module:AlenaTTS

PLUGIN_KEYWORDS = f"Alena plugin {PLUGIN_TYPE}"
PLUGIN_NAMESPACE = f"alena.plugin.{PLUGIN_TYPE}"
PLUGIN_ENTRY_POINT = f"{PLUGIN_MODULE_NAME} = {PLUGIN_TARGET}"

req_file = join(dirname(abspath(__file__)), "requirements.txt")
if exists(req_file):
    with open(req_file) as f:
        requirements = f.readlines()
else:
    requirements = []

setup(
    name="plugin name",
    version="0.1.1",
    description="A plugin for Alena",
    url="http://alena.ru",
    author="Your Name",
    author_email="your@email.ru",
    license="Apache-2.0",
    packages=["package_subdir"],
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=PLUGIN_KEYWORDS,
    entry_points={PLUGIN_NAMESPACE: PLUGIN_ENTRY_POINT},
)
