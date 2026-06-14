# fileWriteFloat

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by writeProfileFloat |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long fileWriteFloat(char section[], char entry[], float def, char file[]); |  |  |  |
| Function | Analogous to fileWriteInt, but writes a float variable to the file instead of a text. |  |  |  |
| Parameters | section Section of file |  |  |  |
| entry Name of variable |  |  |  |  |
| def Value |  |  |  |  |
| file Name of file |  |  |  |  |
| Return Values | 0 if an error has occurred else 1 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | — | • | • |  |
| Example ...if(!fileWriteInt("DeviceData","DeviceAddr",2.2, "TEST.INI"))write("file error");...This call writes the following entry in the file TEST.INI:[DeviceData]DeviceAddr=2.2 |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
