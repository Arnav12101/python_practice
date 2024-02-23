from mymainpackage import some_main_script
from mymainpackage.subpackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()

#__init__.py files are present in the directory so that python would understand that its not some directory but rather its a PACKAGE !