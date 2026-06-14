# fileWriteInt

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by writeProfileInt |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long fileWriteInt(char section[], char entry[], long def, char file[]); |  |  |  |
| Function | Analogous to fileWriteString, but writes a long variable to the file instead of a text. |  |  |  |
| Parameters | section Section of file |  |  |  |
| entry Name of variable |  |  |  |  |
| def Value |  |  |  |  |
| file Name of file |  |  |  |  |
| Return Values | 0 if an error has occurred else 1 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 3.0 | — | • | • |  |
| Example ...if(!fileWriteInt("DeviceData","DeviceAddr",2, "TEST.INI"))write("file error");...This call writes the following entry in the file TEST.INI:[DeviceData]DeviceAddr=2 |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
