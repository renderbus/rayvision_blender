#!/usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import os

def get_script_version():
    return "py" + "".join([str(i) for i in sys.version_info[:2]])

def main():
    task_json = sys.argv[6]
    channel = sys.argv[7]
    RBAnalyze.main(channel,task_json)

if __name__ == "__main__":
    try:
        script_version = get_script_version()
        script_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.insert(0, script_path)

        print("Python executable is: " + sys.executable)
        print("Python version is: " + sys.version)
        sys.stdout.flush()

        exec("from {} import RBAnalyze".format(script_version))
        print("from {} import RBAnalyze".format(script_version))
        main()
    except ImportError as e:
        print("Failed to import module: {}".format(e))
        print("-------------------------------------------")
        print("|                                         |")
        print("| [Error]Blender version is not supported |")
        print("|                                         |")
        print("-------------------------------------------")
        sys.exit(1)
