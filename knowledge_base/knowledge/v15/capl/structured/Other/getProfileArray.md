# getProfileArray

> Category: `Other` | Type: `function`

## Syntax

```c
long getProfileArray(char section[], char entry[],char buff[], long buffsize, char filename[]); // form 1
long getProfileArray(char section[], char entry[],char buff[], long buffsize, char filename[], dword utf16); // form 2
```

## Description

Searches the file under section section for the variable entry. Entry is interpreted as a list of numerical values, separated by comma, tab, space, semicolon or slash. A 0x prefix indicates hex values.

## Parameters

| Name | Description |
|---|---|
| section | Section of the file as a string. |
| entry | Variable name as a string. |
| buff | Buffer for the read-in numerical values. |
| buffsize | Size of buff: Maximum number of read in numerical values (max. 1279 characters). |
| filename | File path as a string. |
| utf16 | If this flag is set the file will be interpreted as UTF-16LE encoded, if the corresponding BOM is also present. |

## Return Values

Number of numerical values read in.

## Example

Note

Using 256 hex values (format 0x??) and int values (format ??? plus signed) respectively as well as separators the string length is 4 * 256 + 255 = 1279 characters.

The first 1279 characters are read from the ini entry and are converted to numerical values.

The above mentioned format is sufficiently for 256 numerical values.

Does the string contain figures with only one figure as well as separators (e.g. 3,1,4,1,5,9,2,6,5,3,5...), 640 numerical values can be read.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0: form 1 12.0: form 2 | 3.0: form 1 12.0: form 2 | 13.0 | — | 14 | 1.0: form 1 4.0: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
