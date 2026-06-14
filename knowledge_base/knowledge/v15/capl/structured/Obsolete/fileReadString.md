# fileReadString

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by getProfileString |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long fileReadString(char section[], char entry[], char def[], char buffer[], long bufferlen, char filename[]); |  |  |  |
| Function | Searches for the variable entry in the section section of the file filename. Its content (value) is written to the buffer buffer. Its length must be passed correctly to bufferlen. If the file or entry is not found, the default value def is copied to buffer. |  |  |  |
| Parameters | section Section of file |  |  |  |
| entry Name of variable |  |  |  |  |
| def Value |  |  |  |  |
| buffer Buffer for characters to be read |  |  |  |  |
| bufferlen Size of buffer in byte |  |  |  |  |
| filename Name of file |  |  |  |  |
| Return Values | Number of bytes read |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | — | • | • |  |
| Example ile TEST.INI:[DATA]NAME=FeldADDR=200FIELD=1,2,3,0x20,100...int len;char buf[20];fileReadString("DATA", "NAME", "DefaultString", buf, elCount(buf), "TEST.INI");... Result: buf is filled with the characters "Feld". |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
