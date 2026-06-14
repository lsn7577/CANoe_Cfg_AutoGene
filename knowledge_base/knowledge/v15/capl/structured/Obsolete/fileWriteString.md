# fileWriteString

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by writeProfileString |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long fileWriteString(char section[], char entry[], char value[], char filename[]); |  |  |  |
| Function | Opens the file filename, finds the section section and writes the variable entry with the value value. If entry already exists, the old value is overwritten. The functional result is the number of characters written, or 0 for an error. |  |  |  |
| Parameters | section Section of file |  |  |  |
| entry Name of variable |  |  |  |  |
| value |  |  |  |  |
| filename Name of file |  |  |  |  |
| Return Values | Number of written characters of 0 if an error has occurred. |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | — | • | • |  |
| Example ...if(!fileWriteString("Device","DeviceName","LPT1","test.ini"))write("file error");...This call writes the following entry in the file TEST.INI:[Device]DeviceName=LPT1 |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
