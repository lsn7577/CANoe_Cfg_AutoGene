# setLogFileName

> Category: `Other` | Type: `function`

## Syntax

```c
setLogFileName(char fileName[]);
```

## Description

Sets the name of the logging file. If a valid extension is given it also changes the file type.

This function is not available in standalone mode.

## Parameters

| Name | Description |
|---|---|
| Note Since CANoe 8.5 the file name can also contain field codes. If the old file name contains only field codes of the auto increment field code type, for downward compatibility new file names will be expanded with the field code of the old file name. The auto increment field codes will be added to the file names as usual. Example field codes: ...setLogFileName( "logFile_M{IncMeasurement}.blf" );...// Sets the name of the logging file to logFile_MX.blf with X = current measurement index....setLogFileName( "logFile_ {Date}.blf" );...// Sets the name of the logging file to logFile_YYYY-MM-DD.blf with YYYY-MM-DD = current system date. |  |

## Return Values

—

## Example

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
```

## Availability

| Since Version |
|---|
