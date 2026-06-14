# String Literal

> Category: `Other` | Type: `notes`

## Description

A string literal is a character string in quotation marks: "This is a character string"

Like in the C language, when storing string literals in char arrays, one char at the end of the array needs to be reserved for the string termination character (/0), i.e. the char array needs to be one element longer than the pure string length.

Certain characters are displayed as a combination of characters with a preceding backslash (escape sequence) within a character string, e.g:

The CAPL string encoding usually matches the encoding of the source file. When you create a file with the CAPL Browser, it will save the file in an encoding which matches the language settings of your computer and write the encoding in a special comment at the beginning of the file. If the source file is encoded in UTF-16 or if an include file has a different encoding than the source file, the CAPL string encoding will be UTF-8.

| Note Like in the C language, when storing string literals in char arrays, one char at the end of the array needs to be reserved for the string termination character (/0), i.e. the char array needs to be one element longer than the pure string length. |
|---|

| Description | Display Inside Character Strings |
|---|---|
| New line | \n |
| Tabulator | \t |
| Backslash | \\ |
| Carriage return | \r |
| Backspace | \b |
| Double quotation mark | \" |
| Single quotation mark | \' |

| Note The CAPL string encoding usually matches the encoding of the source file. When you create a file with the CAPL Browser, it will save the file in an encoding which matches the language settings of your computer and write the encoding in a special comment at the beginning of the file. If the source file is encoded in UTF-16 or if an include file has a different encoding than the source file, the CAPL string encoding will be UTF-8. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
