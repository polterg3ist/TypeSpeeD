# Type-Speed

A console application for testing your typing speed with flexible support for adding new languages and parsers.


Guide how to add new language:

  1. You can directly add a set of words delimited by a newline character (\n)
  2. You can create your own parser for the desired language, which should be located in the folder (TypeSpeeD/parsers). The parser should implement a function named "parse" that will return a list of words. Next you need to run the file "parse_manager.py " select the desired parser and name the file that will be located at path (TypeSpeed/languages). After that, the language will be available for testing.
