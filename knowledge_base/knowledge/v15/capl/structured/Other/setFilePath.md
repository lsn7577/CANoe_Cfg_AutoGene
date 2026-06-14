# setFilePath

> Category: `Other` | Type: `function`

## Syntax

```c
void setFilePath (char Path[],dword mode);
```

## Description

This function sets the read and write path to the directory. The path can be given as absolute or relative to the currently active configuration.

## Parameters

| Name | Description |
|---|---|
| 0 | Sets path for read functions |
| 1 | Sets path for write functions (same as setWritePath) |
| 2 | Sets path for both types of functions |

## Return Values

—

## Example

```c
//set directory for reading
setFilePath("C:\\Windows\\TEMP", 0);
//set directory for writing
setFilePath("D:\\TEMP", 1);
//set directory for writing and reading
setFilePath("C:\\TEMP", 2);

on key 'i'
{
int defaultPara1;
int returnParaInt;
int counter;
double defaultPara2;
double returnParaFloat;
char buffer [256];
//define symbolic values for read/write access mode
dword FILE_PATH_R   = 0;
dword FILE_PATH_W   = 1;
dword FILE_PATH_RW  = 2;
defaultPara1 = -1;
defaultPara2 = -1;
//set absolute file path for writing
setFilePath("C:\\TEMP" , FILE_PATH_W);
// Write different values into the section "Parameter" of the INI file "Test.INI"
// If no file path is specified, the path from previous setFilePath command is used
writeProfileString ("Parameter","String","TestString","Test.INI");
writeProfileFloat ("Parameter","Float", 1.7845,"Test.INI");
writeProfileInt ("Parameter", "Integer", 8, "Test.INI");
// Read different values from the Section "Parameter" of the INI file "C:\\temp\\Test.INI"
// And display the values in the Write Window
//if an absolute path is to be used, this can be coded in the parameter <filename> directly
returnParaInt = getProfileInt("Parameter","Integer",defaultPara1,"C:\\TEMP\\Test.INI");
returnParaFloat = getProFileFloat("Parameter","Float",defaultPara2,"C:\\TEMP\\Test.INI");
getProFileString("Parameter","String","Default String", buffer, elcount(buffer), "C:\\TEMP\\Test.INI");
write("Integer: %d", returnParaInt);
write("Float: %f", returnParaFloat);
write("String: %s", buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.1 | 4.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
