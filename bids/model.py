#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Fri Aug 13 16:11:49 2021 by generateDS.py version 2.39.2.
# Python 3.9.5 (default, May 11 2021, 08:20:37)  [GCC 10.3.0]
#
# Command line options:
#   ('-f', '')
#   ('--member-specs', 'dict')
#   ('--always-export-default', '')
#   ('-o', '../bids/model.py')
#
# Command line arguments:
#   ../schema/bids.xsd
#
# Command line:
#   /home/erdal/Downloads/generateDS-2.39.2/generateDS.py -f --member-specs="dict" --always-export-default -o "../bids/model.py" ../schema/bids.xsd
#
# Current working directory (os.getcwd()):
#   tools
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class JsonOrTsvAllowedExtension(str, Enum):
    TSV='.tsv'
    JSON='.json'


class File(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 0, {'use': 'required'}),
        'extension': MemberSpec_('extension', 'string', 0, 1, {'use': 'optional'}),
        'uri': MemberSpec_('uri', 'anyURI', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, extension=None, uri=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.extension = _cast(None, extension)
        self.extension_nsprefix_ = None
        self.uri = _cast(None, uri)
        self.uri_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, File)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if File.subclass:
            return File.subclass(*args_, **kwargs_)
        else:
            return File(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_extension(self):
        return self.extension
    def set_extension(self, extension):
        self.extension = extension
    def get_uri(self):
        return self.uri
    def set_uri(self, uri):
        self.uri = uri
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='File', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('File')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'File':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='File')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='File', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='File'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.extension is not None and 'extension' not in already_processed:
            already_processed.add('extension')
            outfile.write(' extension=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.extension), input_name='extension')), ))
        if self.uri is not None and 'uri' not in already_processed:
            already_processed.add('uri')
            outfile.write(' uri=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.uri), input_name='uri')), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='File', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('extension', node)
        if value is not None and 'extension' not in already_processed:
            already_processed.add('extension')
            self.extension = value
        value = find_attr_value_('uri', node)
        if value is not None and 'uri' not in already_processed:
            already_processed.add('uri')
            self.uri = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class File


class JsonObject(File):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'properties': MemberSpec_('properties', 'Property', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'properties', 'type': 'Property'}, None),
    }
    subclass = None
    superclass = File
    def __init__(self, name=None, extension=None, uri=None, properties=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("JsonObject"), self).__init__(name, extension, uri, extensiontype_,  **kwargs_)
        if properties is None:
            self.properties = []
        else:
            self.properties = properties
        self.properties_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, JsonObject)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if JsonObject.subclass:
            return JsonObject.subclass(*args_, **kwargs_)
        else:
            return JsonObject(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_properties(self):
        return self.properties
    def set_properties(self, properties):
        self.properties = properties
    def add_properties(self, value):
        self.properties.append(value)
    def insert_properties_at(self, index, value):
        self.properties.insert(index, value)
    def replace_properties_at(self, index, value):
        self.properties[index] = value
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.properties or
            super(JsonObject, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='JsonObject', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('JsonObject')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'JsonObject':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='JsonObject')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='JsonObject', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='JsonObject'):
        super(JsonObject, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='JsonObject')
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='JsonObject', fromsubclass_=False, pretty_print=True):
        super(JsonObject, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for properties_ in self.properties:
            namespaceprefix_ = self.properties_nsprefix_ + ':' if (UseCapturedNS_ and self.properties_nsprefix_) else ''
            properties_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='properties', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(JsonObject, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'properties':
            obj_ = Property.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.properties.append(obj_)
            obj_.original_tagname_ = 'properties'
        super(JsonObject, self)._buildChildren(child_, node, nodeName_, True)
# end class JsonObject


class DatasetDescriptionFile(JsonObject):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'BIDSVersion': MemberSpec_('BIDSVersion', 'string', 0, 0, {'use': 'required'}),
        'Name': MemberSpec_('Name', 'string', 0, 0, {'use': 'required'}),
    }
    subclass = None
    superclass = JsonObject
    def __init__(self, name=None, extension=None, uri=None, properties=None, BIDSVersion=None, Name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DatasetDescriptionFile"), self).__init__(name, extension, uri, properties,  **kwargs_)
        self.BIDSVersion = _cast(None, BIDSVersion)
        self.BIDSVersion_nsprefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DatasetDescriptionFile)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DatasetDescriptionFile.subclass:
            return DatasetDescriptionFile.subclass(*args_, **kwargs_)
        else:
            return DatasetDescriptionFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_BIDSVersion(self):
        return self.BIDSVersion
    def set_BIDSVersion(self, BIDSVersion):
        self.BIDSVersion = BIDSVersion
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            super(DatasetDescriptionFile, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatasetDescriptionFile', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DatasetDescriptionFile')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DatasetDescriptionFile':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatasetDescriptionFile')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DatasetDescriptionFile', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DatasetDescriptionFile'):
        super(DatasetDescriptionFile, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatasetDescriptionFile')
        if self.BIDSVersion is not None and 'BIDSVersion' not in already_processed:
            already_processed.add('BIDSVersion')
            outfile.write(' BIDSVersion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.BIDSVersion), input_name='BIDSVersion')), ))
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatasetDescriptionFile', fromsubclass_=False, pretty_print=True):
        super(DatasetDescriptionFile, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('BIDSVersion', node)
        if value is not None and 'BIDSVersion' not in already_processed:
            already_processed.add('BIDSVersion')
            self.BIDSVersion = value
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
        super(DatasetDescriptionFile, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(DatasetDescriptionFile, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class DatasetDescriptionFile


class Property(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'string', 0, 0, {'use': 'required'}),
        'value': MemberSpec_('value', 'string', 0, 1, {'use': 'optional'}),
        'object': MemberSpec_('object', 'JsonObject', 0, 0, {'name': 'object', 'type': 'JsonObject'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, key=None, value=None, object=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.value = _cast(None, value)
        self.value_nsprefix_ = None
        self.object = object
        self.object_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Property)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Property.subclass:
            return Property.subclass(*args_, **kwargs_)
        else:
            return Property(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_object(self):
        return self.object
    def set_object(self, object):
        self.object = object
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def _hasContent(self):
        if (
            self.object is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Property', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Property')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Property':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Property')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Property', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Property'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')), ))
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.value), input_name='value')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Property', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.object is not None:
            namespaceprefix_ = self.object_nsprefix_ + ':' if (UseCapturedNS_ and self.object_nsprefix_) else ''
            self.object.export(outfile, level, namespaceprefix_, namespacedef_='', name_='object', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'object':
            class_obj_ = self.get_class_obj_(child_, JsonObject)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.object = obj_
            obj_.original_tagname_ = 'object'
# end class Property


class Folder(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 0, {'use': 'required'}),
        'files': MemberSpec_('files', 'File', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'files', 'type': 'File'}, None),
        'folders': MemberSpec_('folders', 'Folder', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'folders', 'type': 'Folder'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, files=None, folders=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        if files is None:
            self.files = []
        else:
            self.files = files
        self.files_nsprefix_ = None
        if folders is None:
            self.folders = []
        else:
            self.folders = folders
        self.folders_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Folder)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Folder.subclass:
            return Folder.subclass(*args_, **kwargs_)
        else:
            return Folder(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_files(self):
        return self.files
    def set_files(self, files):
        self.files = files
    def add_files(self, value):
        self.files.append(value)
    def insert_files_at(self, index, value):
        self.files.insert(index, value)
    def replace_files_at(self, index, value):
        self.files[index] = value
    def get_folders(self):
        return self.folders
    def set_folders(self, folders):
        self.folders = folders
    def add_folders(self, value):
        self.folders.append(value)
    def insert_folders_at(self, index, value):
        self.folders.insert(index, value)
    def replace_folders_at(self, index, value):
        self.folders[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.files or
            self.folders
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Folder', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Folder')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Folder':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Folder')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Folder', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Folder'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Folder', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for files_ in self.files:
            namespaceprefix_ = self.files_nsprefix_ + ':' if (UseCapturedNS_ and self.files_nsprefix_) else ''
            files_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='files', pretty_print=pretty_print)
        for folders_ in self.folders:
            namespaceprefix_ = self.folders_nsprefix_ + ':' if (UseCapturedNS_ and self.folders_nsprefix_) else ''
            folders_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='folders', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'files':
            class_obj_ = self.get_class_obj_(child_, File)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.files.append(obj_)
            obj_.original_tagname_ = 'files'
        elif nodeName_ == 'folders':
            class_obj_ = self.get_class_obj_(child_, Folder)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.folders.append(obj_)
            obj_.original_tagname_ = 'folders'
# end class Folder


class DatatypeFolder(Folder):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'artifacts': MemberSpec_('artifacts', 'Artifact', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'artifacts', 'type': 'Artifact'}, None),
    }
    subclass = None
    superclass = Folder
    def __init__(self, name=None, files=None, folders=None, artifacts=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DatatypeFolder"), self).__init__(name, files, folders,  **kwargs_)
        if artifacts is None:
            self.artifacts = []
        else:
            self.artifacts = artifacts
        self.artifacts_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DatatypeFolder)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DatatypeFolder.subclass:
            return DatatypeFolder.subclass(*args_, **kwargs_)
        else:
            return DatatypeFolder(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_artifacts(self):
        return self.artifacts
    def set_artifacts(self, artifacts):
        self.artifacts = artifacts
    def add_artifacts(self, value):
        self.artifacts.append(value)
    def insert_artifacts_at(self, index, value):
        self.artifacts.insert(index, value)
    def replace_artifacts_at(self, index, value):
        self.artifacts[index] = value
    def _hasContent(self):
        if (
            self.artifacts or
            super(DatatypeFolder, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatatypeFolder', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DatatypeFolder')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DatatypeFolder':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatatypeFolder')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DatatypeFolder', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DatatypeFolder'):
        super(DatatypeFolder, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatatypeFolder')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatatypeFolder', fromsubclass_=False, pretty_print=True):
        super(DatatypeFolder, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for artifacts_ in self.artifacts:
            namespaceprefix_ = self.artifacts_nsprefix_ + ':' if (UseCapturedNS_ and self.artifacts_nsprefix_) else ''
            artifacts_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='artifacts', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DatatypeFolder, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'artifacts':
            obj_ = Artifact.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.artifacts.append(obj_)
            obj_.original_tagname_ = 'artifacts'
        super(DatatypeFolder, self)._buildChildren(child_, node, nodeName_, True)
# end class DatatypeFolder


class Artifact(File):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'suffix': MemberSpec_('suffix', 'string', 0, 0, {'use': 'required'}),
        'entities': MemberSpec_('entities', 'EntityRef', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'entities', 'type': 'EntityRef'}, None),
    }
    subclass = None
    superclass = File
    def __init__(self, name=None, extension=None, uri=None, suffix=None, entities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Artifact"), self).__init__(name, extension, uri,  **kwargs_)
        self.suffix = _cast(None, suffix)
        self.suffix_nsprefix_ = None
        if entities is None:
            self.entities = []
        else:
            self.entities = entities
        self.entities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Artifact)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Artifact.subclass:
            return Artifact.subclass(*args_, **kwargs_)
        else:
            return Artifact(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_entities(self):
        return self.entities
    def set_entities(self, entities):
        self.entities = entities
    def add_entities(self, value):
        self.entities.append(value)
    def insert_entities_at(self, index, value):
        self.entities.insert(index, value)
    def replace_entities_at(self, index, value):
        self.entities[index] = value
    def get_suffix(self):
        return self.suffix
    def set_suffix(self, suffix):
        self.suffix = suffix
    def _hasContent(self):
        if (
            self.entities or
            super(Artifact, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Artifact', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Artifact')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Artifact':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Artifact')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Artifact', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Artifact'):
        super(Artifact, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Artifact')
        if self.suffix is not None and 'suffix' not in already_processed:
            already_processed.add('suffix')
            outfile.write(' suffix=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.suffix), input_name='suffix')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Artifact', fromsubclass_=False, pretty_print=True):
        super(Artifact, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for entities_ in self.entities:
            namespaceprefix_ = self.entities_nsprefix_ + ':' if (UseCapturedNS_ and self.entities_nsprefix_) else ''
            entities_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='entities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('suffix', node)
        if value is not None and 'suffix' not in already_processed:
            already_processed.add('suffix')
            self.suffix = value
        super(Artifact, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'entities':
            obj_ = EntityRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entities.append(obj_)
            obj_.original_tagname_ = 'entities'
        super(Artifact, self)._buildChildren(child_, node, nodeName_, True)
# end class Artifact


class EntityRef(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'string', 0, 1, {'use': 'optional'}),
        'value': MemberSpec_('value', 'string', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, key=None, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.value = _cast(None, value)
        self.value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EntityRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EntityRef.subclass:
            return EntityRef.subclass(*args_, **kwargs_)
        else:
            return EntityRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntityRef', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EntityRef')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EntityRef':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EntityRef')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EntityRef', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EntityRef'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')), ))
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.value), input_name='value')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntityRef', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EntityRef


class Entity(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 0, {'use': 'required'}),
        'label': MemberSpec_('label', 'string', 0, 1, {'use': 'optional'}),
        'key': MemberSpec_('key', 'string', 0, 0, {'use': 'required'}),
        'description': MemberSpec_('description', 'string', 0, 0, {'use': 'required'}),
        'type_': MemberSpec_('type_', 'string', 0, 0, {'use': 'required'}),
        'format': MemberSpec_('format', 'string', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, label=None, key=None, description=None, type_=None, format=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.label = _cast(None, label)
        self.label_nsprefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.format = _cast(None, format)
        self.format_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Entity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Entity.subclass:
            return Entity.subclass(*args_, **kwargs_)
        else:
            return Entity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_format(self):
        return self.format
    def set_format(self, format):
        self.format = format
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Entity', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Entity')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Entity':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Entity')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Entity', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Entity'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.label is not None and 'label' not in already_processed:
            already_processed.add('label')
            outfile.write(' label=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.label), input_name='label')), ))
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')), ))
        if self.description is not None and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.format is not None and 'format' not in already_processed:
            already_processed.add('format')
            outfile.write(' format=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.format), input_name='format')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Entity', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('label', node)
        if value is not None and 'label' not in already_processed:
            already_processed.add('label')
            self.label = value
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('format', node)
        if value is not None and 'format' not in already_processed:
            already_processed.add('format')
            self.format = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Entity


class Suffix(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 0, {'use': 'required'}),
        'description': MemberSpec_('description', 'string', 0, 0, {'use': 'required'}),
        'unit': MemberSpec_('unit', 'string', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, description=None, unit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.unit = _cast(None, unit)
        self.unit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Suffix)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Suffix.subclass:
            return Suffix.subclass(*args_, **kwargs_)
        else:
            return Suffix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Suffix', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Suffix')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Suffix':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Suffix')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Suffix', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Suffix'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.description is not None and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.unit is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            outfile.write(' unit=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.unit), input_name='unit')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Suffix', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('unit', node)
        if value is not None and 'unit' not in already_processed:
            already_processed.add('unit')
            self.unit = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class Suffix


class Modality(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'string', 0, 1, {'use': 'optional'}),
        'name': MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        'datatypes': MemberSpec_('datatypes', 'string', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'datatypes', 'type': 'string'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, key=None, name=None, datatypes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        if datatypes is None:
            self.datatypes = []
        else:
            self.datatypes = datatypes
        self.datatypes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Modality)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Modality.subclass:
            return Modality.subclass(*args_, **kwargs_)
        else:
            return Modality(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_datatypes(self):
        return self.datatypes
    def set_datatypes(self, datatypes):
        self.datatypes = datatypes
    def add_datatypes(self, value):
        self.datatypes.append(value)
    def insert_datatypes_at(self, index, value):
        self.datatypes.insert(index, value)
    def replace_datatypes_at(self, index, value):
        self.datatypes[index] = value
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.datatypes
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='Modality', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Modality')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Modality':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Modality')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Modality', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Modality'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='Modality', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for datatypes_ in self.datatypes:
            namespaceprefix_ = self.datatypes_nsprefix_ + ':' if (UseCapturedNS_ and self.datatypes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdatatypes>%s</%sdatatypes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(datatypes_), input_name='datatypes')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'datatypes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'datatypes')
            value_ = self.gds_validate_string(value_, node, 'datatypes')
            self.datatypes.append(value_)
            self.datatypes_nsprefix_ = child_.prefix
# end class Modality


class Datatype(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        'contexts': MemberSpec_('contexts', 'DatatypeContext', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'contexts', 'type': 'DatatypeContext'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, contexts=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        if contexts is None:
            self.contexts = []
        else:
            self.contexts = contexts
        self.contexts_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Datatype)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Datatype.subclass:
            return Datatype.subclass(*args_, **kwargs_)
        else:
            return Datatype(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contexts(self):
        return self.contexts
    def set_contexts(self, contexts):
        self.contexts = contexts
    def add_contexts(self, value):
        self.contexts.append(value)
    def insert_contexts_at(self, index, value):
        self.contexts.insert(index, value)
    def replace_contexts_at(self, index, value):
        self.contexts[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.contexts
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Datatype', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Datatype')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Datatype':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Datatype')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Datatype', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Datatype'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Datatype', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for contexts_ in self.contexts:
            namespaceprefix_ = self.contexts_nsprefix_ + ':' if (UseCapturedNS_ and self.contexts_nsprefix_) else ''
            contexts_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contexts', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'contexts':
            obj_ = DatatypeContext.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contexts.append(obj_)
            obj_.original_tagname_ = 'contexts'
# end class Datatype


class EntityDep(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'key': MemberSpec_('key', 'string', 0, 0, {'use': 'required'}),
        'required': MemberSpec_('required', 'boolean', 0, 0, {'use': 'required'}),
    }
    subclass = None
    superclass = None
    def __init__(self, key=None, required=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.key = _cast(None, key)
        self.key_nsprefix_ = None
        self.required = _cast(bool, required)
        self.required_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EntityDep)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EntityDep.subclass:
            return EntityDep.subclass(*args_, **kwargs_)
        else:
            return EntityDep(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_key(self):
        return self.key
    def set_key(self, key):
        self.key = key
    def get_required(self):
        return self.required
    def set_required(self, required):
        self.required = required
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntityDep', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EntityDep')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EntityDep':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EntityDep')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EntityDep', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EntityDep'):
        if self.key is not None and 'key' not in already_processed:
            already_processed.add('key')
            outfile.write(' key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.key), input_name='key')), ))
        if self.required is not None and 'required' not in already_processed:
            already_processed.add('required')
            outfile.write(' required="%s"' % self.gds_format_boolean(self.required, input_name='required'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntityDep', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('key', node)
        if value is not None and 'key' not in already_processed:
            already_processed.add('key')
            self.key = value
        value = find_attr_value_('required', node)
        if value is not None and 'required' not in already_processed:
            already_processed.add('required')
            if value in ('true', '1'):
                self.required = True
            elif value in ('false', '0'):
                self.required = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EntityDep


class EntitiesContainer(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'entities': MemberSpec_('entities', 'Entity', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'entities', 'type': 'Entity'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, entities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if entities is None:
            self.entities = []
        else:
            self.entities = entities
        self.entities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EntitiesContainer)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EntitiesContainer.subclass:
            return EntitiesContainer.subclass(*args_, **kwargs_)
        else:
            return EntitiesContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_entities(self):
        return self.entities
    def set_entities(self, entities):
        self.entities = entities
    def add_entities(self, value):
        self.entities.append(value)
    def insert_entities_at(self, index, value):
        self.entities.insert(index, value)
    def replace_entities_at(self, index, value):
        self.entities[index] = value
    def _hasContent(self):
        if (
            self.entities
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntitiesContainer', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EntitiesContainer')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EntitiesContainer':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EntitiesContainer')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EntitiesContainer', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EntitiesContainer'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='EntitiesContainer', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for entities_ in self.entities:
            namespaceprefix_ = self.entities_nsprefix_ + ':' if (UseCapturedNS_ and self.entities_nsprefix_) else ''
            entities_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='entities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'entities':
            obj_ = Entity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entities.append(obj_)
            obj_.original_tagname_ = 'entities'
# end class EntitiesContainer


class ModalitiesContainer(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'modalities': MemberSpec_('modalities', 'Modality', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'modalities', 'type': 'Modality'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, modalities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if modalities is None:
            self.modalities = []
        else:
            self.modalities = modalities
        self.modalities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ModalitiesContainer)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ModalitiesContainer.subclass:
            return ModalitiesContainer.subclass(*args_, **kwargs_)
        else:
            return ModalitiesContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_modalities(self):
        return self.modalities
    def set_modalities(self, modalities):
        self.modalities = modalities
    def add_modalities(self, value):
        self.modalities.append(value)
    def insert_modalities_at(self, index, value):
        self.modalities.insert(index, value)
    def replace_modalities_at(self, index, value):
        self.modalities[index] = value
    def _hasContent(self):
        if (
            self.modalities
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='ModalitiesContainer', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ModalitiesContainer')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ModalitiesContainer':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ModalitiesContainer')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ModalitiesContainer', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ModalitiesContainer'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='ModalitiesContainer', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for modalities_ in self.modalities:
            namespaceprefix_ = self.modalities_nsprefix_ + ':' if (UseCapturedNS_ and self.modalities_nsprefix_) else ''
            modalities_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='modalities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'modalities':
            obj_ = Modality.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.modalities.append(obj_)
            obj_.original_tagname_ = 'modalities'
# end class ModalitiesContainer


class DatatypesContainer(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'datatypes': MemberSpec_('datatypes', 'Datatype', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'datatypes', 'type': 'Datatype'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, datatypes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if datatypes is None:
            self.datatypes = []
        else:
            self.datatypes = datatypes
        self.datatypes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DatatypesContainer)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DatatypesContainer.subclass:
            return DatatypesContainer.subclass(*args_, **kwargs_)
        else:
            return DatatypesContainer(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_datatypes(self):
        return self.datatypes
    def set_datatypes(self, datatypes):
        self.datatypes = datatypes
    def add_datatypes(self, value):
        self.datatypes.append(value)
    def insert_datatypes_at(self, index, value):
        self.datatypes.insert(index, value)
    def replace_datatypes_at(self, index, value):
        self.datatypes[index] = value
    def _hasContent(self):
        if (
            self.datatypes
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatatypesContainer', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DatatypesContainer')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DatatypesContainer':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatatypesContainer')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DatatypesContainer', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DatatypesContainer'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DatatypesContainer', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for datatypes_ in self.datatypes:
            namespaceprefix_ = self.datatypes_nsprefix_ + ':' if (UseCapturedNS_ and self.datatypes_nsprefix_) else ''
            datatypes_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='datatypes', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'datatypes':
            obj_ = Datatype.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.datatypes.append(obj_)
            obj_.original_tagname_ = 'datatypes'
# end class DatatypesContainer


class DatatypeContext(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        'suffixes': MemberSpec_('suffixes', 'string', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'suffixes', 'type': 'string'}, None),
        'extensions': MemberSpec_('extensions', 'string', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'extensions', 'type': 'string'}, None),
        'entities': MemberSpec_('entities', 'EntityDep', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'entities', 'type': 'EntityDep'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, suffixes=None, extensions=None, entities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        if suffixes is None:
            self.suffixes = []
        else:
            self.suffixes = suffixes
        self.suffixes_nsprefix_ = None
        if extensions is None:
            self.extensions = []
        else:
            self.extensions = extensions
        self.extensions_nsprefix_ = None
        if entities is None:
            self.entities = []
        else:
            self.entities = entities
        self.entities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DatatypeContext)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DatatypeContext.subclass:
            return DatatypeContext.subclass(*args_, **kwargs_)
        else:
            return DatatypeContext(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_suffixes(self):
        return self.suffixes
    def set_suffixes(self, suffixes):
        self.suffixes = suffixes
    def add_suffixes(self, value):
        self.suffixes.append(value)
    def insert_suffixes_at(self, index, value):
        self.suffixes.insert(index, value)
    def replace_suffixes_at(self, index, value):
        self.suffixes[index] = value
    def get_extensions(self):
        return self.extensions
    def set_extensions(self, extensions):
        self.extensions = extensions
    def add_extensions(self, value):
        self.extensions.append(value)
    def insert_extensions_at(self, index, value):
        self.extensions.insert(index, value)
    def replace_extensions_at(self, index, value):
        self.extensions[index] = value
    def get_entities(self):
        return self.entities
    def set_entities(self, entities):
        self.entities = entities
    def add_entities(self, value):
        self.entities.append(value)
    def insert_entities_at(self, index, value):
        self.entities.insert(index, value)
    def replace_entities_at(self, index, value):
        self.entities[index] = value
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def _hasContent(self):
        if (
            self.suffixes or
            self.extensions or
            self.entities
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DatatypeContext', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DatatypeContext')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DatatypeContext':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DatatypeContext')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DatatypeContext', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DatatypeContext'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='DatatypeContext', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for suffixes_ in self.suffixes:
            namespaceprefix_ = self.suffixes_nsprefix_ + ':' if (UseCapturedNS_ and self.suffixes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssuffixes>%s</%ssuffixes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(suffixes_), input_name='suffixes')), namespaceprefix_ , eol_))
        for extensions_ in self.extensions:
            namespaceprefix_ = self.extensions_nsprefix_ + ':' if (UseCapturedNS_ and self.extensions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sextensions>%s</%sextensions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(extensions_), input_name='extensions')), namespaceprefix_ , eol_))
        for entities_ in self.entities:
            namespaceprefix_ = self.entities_nsprefix_ + ':' if (UseCapturedNS_ and self.entities_nsprefix_) else ''
            entities_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='entities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'suffixes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'suffixes')
            value_ = self.gds_validate_string(value_, node, 'suffixes')
            self.suffixes.append(value_)
            self.suffixes_nsprefix_ = child_.prefix
        elif nodeName_ == 'extensions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'extensions')
            value_ = self.gds_validate_string(value_, node, 'extensions')
            self.extensions.append(value_)
            self.extensions_nsprefix_ = child_.prefix
        elif nodeName_ == 'entities':
            obj_ = EntityDep.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entities.append(obj_)
            obj_.original_tagname_ = 'entities'
# end class DatatypeContext


class Metadata(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'datatypes': MemberSpec_('datatypes', 'DatatypesContainer', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'datatypes', 'type': 'DatatypesContainer'}, None),
        'entities': MemberSpec_('entities', 'EntitiesContainer', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'entities', 'type': 'EntitiesContainer'}, None),
        'modalities': MemberSpec_('modalities', 'ModalitiesContainer', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'modalities', 'type': 'ModalitiesContainer'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, datatypes=None, entities=None, modalities=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.datatypes = datatypes
        self.datatypes_nsprefix_ = None
        self.entities = entities
        self.entities_nsprefix_ = None
        self.modalities = modalities
        self.modalities_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Metadata)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Metadata.subclass:
            return Metadata.subclass(*args_, **kwargs_)
        else:
            return Metadata(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_datatypes(self):
        return self.datatypes
    def set_datatypes(self, datatypes):
        self.datatypes = datatypes
    def get_entities(self):
        return self.entities
    def set_entities(self, entities):
        self.entities = entities
    def get_modalities(self):
        return self.modalities
    def set_modalities(self, modalities):
        self.modalities = modalities
    def _hasContent(self):
        if (
            self.datatypes is not None or
            self.entities is not None or
            self.modalities is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Metadata', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Metadata')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Metadata':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Metadata')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Metadata', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Metadata'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Metadata', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.datatypes is not None:
            namespaceprefix_ = self.datatypes_nsprefix_ + ':' if (UseCapturedNS_ and self.datatypes_nsprefix_) else ''
            self.datatypes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='datatypes', pretty_print=pretty_print)
        if self.entities is not None:
            namespaceprefix_ = self.entities_nsprefix_ + ':' if (UseCapturedNS_ and self.entities_nsprefix_) else ''
            self.entities.export(outfile, level, namespaceprefix_, namespacedef_='', name_='entities', pretty_print=pretty_print)
        if self.modalities is not None:
            namespaceprefix_ = self.modalities_nsprefix_ + ':' if (UseCapturedNS_ and self.modalities_nsprefix_) else ''
            self.modalities.export(outfile, level, namespaceprefix_, namespacedef_='', name_='modalities', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'datatypes':
            obj_ = DatatypesContainer.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.datatypes = obj_
            obj_.original_tagname_ = 'datatypes'
        elif nodeName_ == 'entities':
            obj_ = EntitiesContainer.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.entities = obj_
            obj_.original_tagname_ = 'entities'
        elif nodeName_ == 'modalities':
            obj_ = ModalitiesContainer.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.modalities = obj_
            obj_.original_tagname_ = 'modalities'
# end class Metadata


class DataframeObject(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'columns': MemberSpec_('columns', 'DataframeColumn', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'columns', 'type': 'DataframeColumn'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, columns=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if columns is None:
            self.columns = []
        else:
            self.columns = columns
        self.columns_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DataframeObject)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DataframeObject.subclass:
            return DataframeObject.subclass(*args_, **kwargs_)
        else:
            return DataframeObject(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_columns(self):
        return self.columns
    def set_columns(self, columns):
        self.columns = columns
    def add_columns(self, value):
        self.columns.append(value)
    def insert_columns_at(self, index, value):
        self.columns.insert(index, value)
    def replace_columns_at(self, index, value):
        self.columns[index] = value
    def _hasContent(self):
        if (
            self.columns
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DataframeObject', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DataframeObject')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DataframeObject':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DataframeObject')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DataframeObject', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DataframeObject'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DataframeObject', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for columns_ in self.columns:
            namespaceprefix_ = self.columns_nsprefix_ + ':' if (UseCapturedNS_ and self.columns_nsprefix_) else ''
            columns_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='columns', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'columns':
            obj_ = DataframeColumn.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.columns.append(obj_)
            obj_.original_tagname_ = 'columns'
# end class DataframeObject


class DataframeColumn(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        'type_': MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, name=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DataframeColumn)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DataframeColumn.subclass:
            return DataframeColumn.subclass(*args_, **kwargs_)
        else:
            return DataframeColumn(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DataframeColumn', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DataframeColumn')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DataframeColumn':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DataframeColumn')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DataframeColumn', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DataframeColumn'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='DataframeColumn', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DataframeColumn


class ParticipantsFile(File):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'allowedExtensions': MemberSpec_('allowedExtensions', 'bids:JsonOrTsvAllowedExtension', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = File
    def __init__(self, name=None, extension=None, uri=None, allowedExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ParticipantsFile"), self).__init__(name, extension, uri,  **kwargs_)
        self.allowedExtensions = _cast(None, allowedExtensions)
        self.allowedExtensions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParticipantsFile)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParticipantsFile.subclass:
            return ParticipantsFile.subclass(*args_, **kwargs_)
        else:
            return ParticipantsFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_allowedExtensions(self):
        return self.allowedExtensions
    def set_allowedExtensions(self, allowedExtensions):
        self.allowedExtensions = allowedExtensions
    def validate_JsonOrTsvAllowedExtension(self, value):
        # Validate type bids:JsonOrTsvAllowedExtension, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['.tsv', '.json']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on JsonOrTsvAllowedExtension' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            super(ParticipantsFile, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='ParticipantsFile', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParticipantsFile')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParticipantsFile':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticipantsFile')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParticipantsFile', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParticipantsFile'):
        super(ParticipantsFile, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParticipantsFile')
        if self.allowedExtensions is not None and 'allowedExtensions' not in already_processed:
            already_processed.add('allowedExtensions')
            outfile.write(' allowedExtensions=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.allowedExtensions), input_name='allowedExtensions')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='ParticipantsFile', fromsubclass_=False, pretty_print=True):
        super(ParticipantsFile, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('allowedExtensions', node)
        if value is not None and 'allowedExtensions' not in already_processed:
            already_processed.add('allowedExtensions')
            self.allowedExtensions = value
            self.validate_JsonOrTsvAllowedExtension(self.allowedExtensions)    # validate type JsonOrTsvAllowedExtension
        super(ParticipantsFile, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ParticipantsFile, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ParticipantsFile


class SamplesFile(File):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'allowedExtensions': MemberSpec_('allowedExtensions', 'bids:JsonOrTsvAllowedExtension', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = File
    def __init__(self, name=None, extension=None, uri=None, allowedExtensions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("SamplesFile"), self).__init__(name, extension, uri,  **kwargs_)
        self.allowedExtensions = _cast(None, allowedExtensions)
        self.allowedExtensions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SamplesFile)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SamplesFile.subclass:
            return SamplesFile.subclass(*args_, **kwargs_)
        else:
            return SamplesFile(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_allowedExtensions(self):
        return self.allowedExtensions
    def set_allowedExtensions(self, allowedExtensions):
        self.allowedExtensions = allowedExtensions
    def validate_JsonOrTsvAllowedExtension(self, value):
        # Validate type bids:JsonOrTsvAllowedExtension, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['.tsv', '.json']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on JsonOrTsvAllowedExtension' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def _hasContent(self):
        if (
            super(SamplesFile, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='SamplesFile', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SamplesFile')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SamplesFile':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SamplesFile')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SamplesFile', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SamplesFile'):
        super(SamplesFile, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SamplesFile')
        if self.allowedExtensions is not None and 'allowedExtensions' not in already_processed:
            already_processed.add('allowedExtensions')
            outfile.write(' allowedExtensions=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.allowedExtensions), input_name='allowedExtensions')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='SamplesFile', fromsubclass_=False, pretty_print=True):
        super(SamplesFile, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('allowedExtensions', node)
        if value is not None and 'allowedExtensions' not in already_processed:
            already_processed.add('allowedExtensions')
            self.allowedExtensions = value
            self.validate_JsonOrTsvAllowedExtension(self.allowedExtensions)    # validate type JsonOrTsvAllowedExtension
        super(SamplesFile, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(SamplesFile, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class SamplesFile


class Session(Folder):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'datatypes': MemberSpec_('datatypes', 'DatatypeFolder', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'datatypes', 'type': 'DatatypeFolder'}, None),
    }
    subclass = None
    superclass = Folder
    def __init__(self, name=None, files=None, folders=None, datatypes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Session"), self).__init__(name, files, folders,  **kwargs_)
        if datatypes is None:
            self.datatypes = []
        else:
            self.datatypes = datatypes
        self.datatypes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Session)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Session.subclass:
            return Session.subclass(*args_, **kwargs_)
        else:
            return Session(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_datatypes(self):
        return self.datatypes
    def set_datatypes(self, datatypes):
        self.datatypes = datatypes
    def add_datatypes(self, value):
        self.datatypes.append(value)
    def insert_datatypes_at(self, index, value):
        self.datatypes.insert(index, value)
    def replace_datatypes_at(self, index, value):
        self.datatypes[index] = value
    def _hasContent(self):
        if (
            self.datatypes or
            super(Session, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Session', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Session')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Session':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Session')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Session', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Session'):
        super(Session, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Session')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Session', fromsubclass_=False, pretty_print=True):
        super(Session, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for datatypes_ in self.datatypes:
            namespaceprefix_ = self.datatypes_nsprefix_ + ':' if (UseCapturedNS_ and self.datatypes_nsprefix_) else ''
            datatypes_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='datatypes', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Session, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'datatypes':
            obj_ = DatatypeFolder.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.datatypes.append(obj_)
            obj_.original_tagname_ = 'datatypes'
        super(Session, self)._buildChildren(child_, node, nodeName_, True)
# end class Session


class Subject(Folder):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'sessions': MemberSpec_('sessions', 'Session', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'sessions', 'type': 'Session'}, 1),
        'datatypes': MemberSpec_('datatypes', 'DatatypeFolder', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'datatypes', 'type': 'DatatypeFolder'}, 1),
    }
    subclass = None
    superclass = Folder
    def __init__(self, name=None, files=None, folders=None, sessions=None, datatypes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Subject"), self).__init__(name, files, folders,  **kwargs_)
        if sessions is None:
            self.sessions = []
        else:
            self.sessions = sessions
        self.sessions_nsprefix_ = None
        if datatypes is None:
            self.datatypes = []
        else:
            self.datatypes = datatypes
        self.datatypes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Subject)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Subject.subclass:
            return Subject.subclass(*args_, **kwargs_)
        else:
            return Subject(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_sessions(self):
        return self.sessions
    def set_sessions(self, sessions):
        self.sessions = sessions
    def add_sessions(self, value):
        self.sessions.append(value)
    def insert_sessions_at(self, index, value):
        self.sessions.insert(index, value)
    def replace_sessions_at(self, index, value):
        self.sessions[index] = value
    def get_datatypes(self):
        return self.datatypes
    def set_datatypes(self, datatypes):
        self.datatypes = datatypes
    def add_datatypes(self, value):
        self.datatypes.append(value)
    def insert_datatypes_at(self, index, value):
        self.datatypes.insert(index, value)
    def replace_datatypes_at(self, index, value):
        self.datatypes[index] = value
    def _hasContent(self):
        if (
            self.sessions or
            self.datatypes or
            super(Subject, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Subject', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Subject')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Subject':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Subject')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Subject', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Subject'):
        super(Subject, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Subject')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Subject', fromsubclass_=False, pretty_print=True):
        super(Subject, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for sessions_ in self.sessions:
            namespaceprefix_ = self.sessions_nsprefix_ + ':' if (UseCapturedNS_ and self.sessions_nsprefix_) else ''
            sessions_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sessions', pretty_print=pretty_print)
        for datatypes_ in self.datatypes:
            namespaceprefix_ = self.datatypes_nsprefix_ + ':' if (UseCapturedNS_ and self.datatypes_nsprefix_) else ''
            datatypes_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='datatypes', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(Subject, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'sessions':
            obj_ = Session.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sessions.append(obj_)
            obj_.original_tagname_ = 'sessions'
        elif nodeName_ == 'datatypes':
            obj_ = DatatypeFolder.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.datatypes.append(obj_)
            obj_.original_tagname_ = 'datatypes'
        super(Subject, self)._buildChildren(child_, node, nodeName_, True)
# end class Subject


class Dataset(Folder):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'base': MemberSpec_('base', 'string', 0, 0, {'use': 'required'}),
        'subjects': MemberSpec_('subjects', 'Subject', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'subjects', 'type': 'Subject'}, None),
        'dataset_description': MemberSpec_('dataset_description', 'DatasetDescriptionFile', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dataset_description', 'type': 'DatasetDescriptionFile'}, None),
        'README': MemberSpec_('README', 'File', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'README', 'type': 'File'}, None),
        'CHANGES': MemberSpec_('CHANGES', 'File', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CHANGES', 'type': 'File'}, None),
        'LICENSE': MemberSpec_('LICENSE', 'File', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'LICENSE', 'type': 'File'}, None),
        'genetic_info': MemberSpec_('genetic_info', 'JsonObject', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'genetic_info', 'type': 'JsonObject'}, None),
        'participants': MemberSpec_('participants', 'ParticipantsFile', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'participants', 'type': 'ParticipantsFile'}, None),
        'samples': MemberSpec_('samples', 'SamplesFile', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'samples', 'type': 'SamplesFile'}, None),
        'stimuli': MemberSpec_('stimuli', 'Folder', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'stimuli', 'type': 'Folder'}, None),
        'code': MemberSpec_('code', 'Folder', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'code', 'type': 'Folder'}, None),
        'derivatives': MemberSpec_('derivatives', 'Folder', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'derivatives', 'type': 'Folder'}, None),
        'sourcedata': MemberSpec_('sourcedata', 'Folder', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'sourcedata', 'type': 'Folder'}, None),
    }
    subclass = None
    superclass = Folder
    def __init__(self, name=None, files=None, folders=None, base=None, subjects=None, dataset_description=None, README=None, CHANGES=None, LICENSE=None, genetic_info=None, participants=None, samples=None, stimuli=None, code=None, derivatives=None, sourcedata=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("Dataset"), self).__init__(name, files, folders,  **kwargs_)
        self.base = _cast(None, base)
        self.base_nsprefix_ = None
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects
        self.subjects_nsprefix_ = None
        self.dataset_description = dataset_description
        self.dataset_description_nsprefix_ = None
        self.README = README
        self.README_nsprefix_ = None
        self.CHANGES = CHANGES
        self.CHANGES_nsprefix_ = None
        self.LICENSE = LICENSE
        self.LICENSE_nsprefix_ = None
        self.genetic_info = genetic_info
        self.genetic_info_nsprefix_ = None
        self.participants = participants
        self.participants_nsprefix_ = None
        self.samples = samples
        self.samples_nsprefix_ = None
        self.stimuli = stimuli
        self.stimuli_nsprefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.derivatives = derivatives
        self.derivatives_nsprefix_ = None
        self.sourcedata = sourcedata
        self.sourcedata_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Dataset)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Dataset.subclass:
            return Dataset.subclass(*args_, **kwargs_)
        else:
            return Dataset(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_subjects(self):
        return self.subjects
    def set_subjects(self, subjects):
        self.subjects = subjects
    def add_subjects(self, value):
        self.subjects.append(value)
    def insert_subjects_at(self, index, value):
        self.subjects.insert(index, value)
    def replace_subjects_at(self, index, value):
        self.subjects[index] = value
    def get_dataset_description(self):
        return self.dataset_description
    def set_dataset_description(self, dataset_description):
        self.dataset_description = dataset_description
    def get_README(self):
        return self.README
    def set_README(self, README):
        self.README = README
    def get_CHANGES(self):
        return self.CHANGES
    def set_CHANGES(self, CHANGES):
        self.CHANGES = CHANGES
    def get_LICENSE(self):
        return self.LICENSE
    def set_LICENSE(self, LICENSE):
        self.LICENSE = LICENSE
    def get_genetic_info(self):
        return self.genetic_info
    def set_genetic_info(self, genetic_info):
        self.genetic_info = genetic_info
    def get_participants(self):
        return self.participants
    def set_participants(self, participants):
        self.participants = participants
    def get_samples(self):
        return self.samples
    def set_samples(self, samples):
        self.samples = samples
    def get_stimuli(self):
        return self.stimuli
    def set_stimuli(self, stimuli):
        self.stimuli = stimuli
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_derivatives(self):
        return self.derivatives
    def set_derivatives(self, derivatives):
        self.derivatives = derivatives
    def get_sourcedata(self):
        return self.sourcedata
    def set_sourcedata(self, sourcedata):
        self.sourcedata = sourcedata
    def get_base(self):
        return self.base
    def set_base(self, base):
        self.base = base
    def _hasContent(self):
        if (
            self.subjects or
            self.dataset_description is not None or
            self.README is not None or
            self.CHANGES is not None or
            self.LICENSE is not None or
            self.genetic_info is not None or
            self.participants is not None or
            self.samples is not None or
            self.stimuli is not None or
            self.code is not None or
            self.derivatives is not None or
            self.sourcedata is not None or
            super(Dataset, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Dataset', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Dataset')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'Dataset':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dataset')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Dataset', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Dataset'):
        super(Dataset, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Dataset')
        if self.base is not None and 'base' not in already_processed:
            already_processed.add('base')
            outfile.write(' base=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.base), input_name='base')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"', name_='Dataset', fromsubclass_=False, pretty_print=True):
        super(Dataset, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for subjects_ in self.subjects:
            namespaceprefix_ = self.subjects_nsprefix_ + ':' if (UseCapturedNS_ and self.subjects_nsprefix_) else ''
            subjects_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='subjects', pretty_print=pretty_print)
        if self.dataset_description is not None:
            namespaceprefix_ = self.dataset_description_nsprefix_ + ':' if (UseCapturedNS_ and self.dataset_description_nsprefix_) else ''
            self.dataset_description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dataset_description', pretty_print=pretty_print)
        if self.README is not None:
            namespaceprefix_ = self.README_nsprefix_ + ':' if (UseCapturedNS_ and self.README_nsprefix_) else ''
            self.README.export(outfile, level, namespaceprefix_, namespacedef_='', name_='README', pretty_print=pretty_print)
        if self.CHANGES is not None:
            namespaceprefix_ = self.CHANGES_nsprefix_ + ':' if (UseCapturedNS_ and self.CHANGES_nsprefix_) else ''
            self.CHANGES.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CHANGES', pretty_print=pretty_print)
        if self.LICENSE is not None:
            namespaceprefix_ = self.LICENSE_nsprefix_ + ':' if (UseCapturedNS_ and self.LICENSE_nsprefix_) else ''
            self.LICENSE.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LICENSE', pretty_print=pretty_print)
        if self.genetic_info is not None:
            namespaceprefix_ = self.genetic_info_nsprefix_ + ':' if (UseCapturedNS_ and self.genetic_info_nsprefix_) else ''
            self.genetic_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='genetic_info', pretty_print=pretty_print)
        if self.participants is not None:
            namespaceprefix_ = self.participants_nsprefix_ + ':' if (UseCapturedNS_ and self.participants_nsprefix_) else ''
            self.participants.export(outfile, level, namespaceprefix_, namespacedef_='', name_='participants', pretty_print=pretty_print)
        if self.samples is not None:
            namespaceprefix_ = self.samples_nsprefix_ + ':' if (UseCapturedNS_ and self.samples_nsprefix_) else ''
            self.samples.export(outfile, level, namespaceprefix_, namespacedef_='', name_='samples', pretty_print=pretty_print)
        if self.stimuli is not None:
            namespaceprefix_ = self.stimuli_nsprefix_ + ':' if (UseCapturedNS_ and self.stimuli_nsprefix_) else ''
            self.stimuli.export(outfile, level, namespaceprefix_, namespacedef_='', name_='stimuli', pretty_print=pretty_print)
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            self.code.export(outfile, level, namespaceprefix_, namespacedef_='', name_='code', pretty_print=pretty_print)
        if self.derivatives is not None:
            namespaceprefix_ = self.derivatives_nsprefix_ + ':' if (UseCapturedNS_ and self.derivatives_nsprefix_) else ''
            self.derivatives.export(outfile, level, namespaceprefix_, namespacedef_='', name_='derivatives', pretty_print=pretty_print)
        if self.sourcedata is not None:
            namespaceprefix_ = self.sourcedata_nsprefix_ + ':' if (UseCapturedNS_ and self.sourcedata_nsprefix_) else ''
            self.sourcedata.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sourcedata', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('base', node)
        if value is not None and 'base' not in already_processed:
            already_processed.add('base')
            self.base = value
        super(Dataset, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'subjects':
            obj_ = Subject.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.subjects.append(obj_)
            obj_.original_tagname_ = 'subjects'
        elif nodeName_ == 'dataset_description':
            obj_ = DatasetDescriptionFile.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dataset_description = obj_
            obj_.original_tagname_ = 'dataset_description'
        elif nodeName_ == 'README':
            class_obj_ = self.get_class_obj_(child_, File)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.README = obj_
            obj_.original_tagname_ = 'README'
        elif nodeName_ == 'CHANGES':
            class_obj_ = self.get_class_obj_(child_, File)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CHANGES = obj_
            obj_.original_tagname_ = 'CHANGES'
        elif nodeName_ == 'LICENSE':
            class_obj_ = self.get_class_obj_(child_, File)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LICENSE = obj_
            obj_.original_tagname_ = 'LICENSE'
        elif nodeName_ == 'genetic_info':
            class_obj_ = self.get_class_obj_(child_, JsonObject)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.genetic_info = obj_
            obj_.original_tagname_ = 'genetic_info'
        elif nodeName_ == 'participants':
            obj_ = ParticipantsFile.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.participants = obj_
            obj_.original_tagname_ = 'participants'
        elif nodeName_ == 'samples':
            obj_ = SamplesFile.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.samples = obj_
            obj_.original_tagname_ = 'samples'
        elif nodeName_ == 'stimuli':
            class_obj_ = self.get_class_obj_(child_, Folder)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.stimuli = obj_
            obj_.original_tagname_ = 'stimuli'
        elif nodeName_ == 'code':
            class_obj_ = self.get_class_obj_(child_, Folder)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.code = obj_
            obj_.original_tagname_ = 'code'
        elif nodeName_ == 'derivatives':
            class_obj_ = self.get_class_obj_(child_, Folder)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.derivatives = obj_
            obj_.original_tagname_ = 'derivatives'
        elif nodeName_ == 'sourcedata':
            class_obj_ = self.get_class_obj_(child_, Folder)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sourcedata = obj_
            obj_.original_tagname_ = 'sourcedata'
        super(Dataset, self)._buildChildren(child_, node, nodeName_, True)
# end class Dataset


GDSClassesMapping = {
    'dataset': Dataset,
    'metadata': Metadata,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Dataset'
        rootClass = Dataset
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Dataset'
        rootClass = Dataset
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Dataset'
        rootClass = Dataset
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:bids="https://bids.neuroimaging.io/1.7.0"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Dataset'
        rootClass = Dataset
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from model import *\n\n')
        sys.stdout.write('import model as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'https://bids.neuroimaging.io/1.7.0': [('JsonOrTsvAllowedExtension',
                                         '../schema/bids.xsd',
                                         'ST'),
                                        ('Dataset', '../schema/bids.xsd', 'CT'),
                                        ('Subject', '../schema/bids.xsd', 'CT'),
                                        ('Session', '../schema/bids.xsd', 'CT'),
                                        ('File', '../schema/bids.xsd', 'CT'),
                                        ('JsonObject',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('DatasetDescriptionFile',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Property',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Folder', '../schema/bids.xsd', 'CT'),
                                        ('DatatypeFolder',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Artifact',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('EntityRef',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Entity', '../schema/bids.xsd', 'CT'),
                                        ('Suffix', '../schema/bids.xsd', 'CT'),
                                        ('Modality',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Datatype',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('EntityDep',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('EntitiesContainer',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('ModalitiesContainer',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('DatatypesContainer',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('DatatypeContext',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('Metadata',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('DataframeObject',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('DataframeColumn',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('ParticipantsFile',
                                         '../schema/bids.xsd',
                                         'CT'),
                                        ('SamplesFile',
                                         '../schema/bids.xsd',
                                         'CT')]}

__all__ = [
    "Artifact",
    "DataframeColumn",
    "DataframeObject",
    "Dataset",
    "DatasetDescriptionFile",
    "Datatype",
    "DatatypeContext",
    "DatatypeFolder",
    "DatatypesContainer",
    "EntitiesContainer",
    "Entity",
    "EntityDep",
    "EntityRef",
    "File",
    "Folder",
    "JsonObject",
    "Metadata",
    "ModalitiesContainer",
    "Modality",
    "ParticipantsFile",
    "Property",
    "SamplesFile",
    "Session",
    "Subject",
    "Suffix"
]
