# setLogFileName

> Category: `Other` | Type: `function`

## Syntax

```c
setLogFileName(char fileName[]); // form 1
setLogFileName(char strLoggingBlockName[], char fileName[]); // form 2
```

## Description

Sets the name of the logging file. If a valid extension is given it also changes the file type.

## Parameters

| Name | Description |
|---|---|
| Note Since CANoe 8.5 the file name can also contain field codes. If the old file name contains only field codes of the auto increment field code type, for downward compatibility new file names will be expanded with the field code of the old file name. The auto increment field codes will be added to the file names as usual. Example field codes: ...setLogFileName( "logFile_M{IncMeasurement}.blf" );...// Sets the name of the logging file to logFile_MX.blf with X = current measurement index....setLogFileName( "logFile_ {Date}.blf" );...// Sets the name of the logging file to logFile_YYYY-MM-DD.blf with YYYY-MM-DD = current system date. |  |
| Note Within a string literal a second backslash has to be set (see example). |  |
| Note The name set with the setLogFileName function will not be saved when saving the configuration. Only the name set in the configuration dialog of the logging file will be taken over. |  |
| strLoggingBlockName | Name of the Logging Block. |

## Return Values

—

## Example

Example File Type

```c
...
setLogFileName("Logging1", "newlog");
...
Sets the name of the logging file to "newlog" in the directory of the current configuration.
...
setLogFileName("Logging1", "c:\\canw\\demo\\automot\\newlog");
...
Sets the absolute path of the logging file.
...
setLogFileName("Logging1", "..\\Logging\\newlog");
...
Sets the relative path of the logging file.
...
setLogFileName( "newlog.blf" );
...
Sets the name of the logging file to newlog and the file type  blf
...
...
setLogFileName( "newlog.notSupportedExtension" );
...
Does nothing //file extension not valid
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All: form 1 7.6 SP3: form 2 | All: form 1 7.6 SP3: form 2 | 13.0 | 13.0: form 1 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
