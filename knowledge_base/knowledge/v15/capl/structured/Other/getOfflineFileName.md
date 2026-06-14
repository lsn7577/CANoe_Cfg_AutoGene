# getOfflineFileName

> Category: `Other` | Type: `function`

## Syntax

```c
long getOfflineFileName(char[] buffer, dword bufferSize); //form 1
long getOfflineFileName(long index, char[] buffer, dword bufferSize); // form 2
```

## Description

Returns the complete path of one file of the currently used offline source files. If form 1 is used, the first file is returned, otherwise the index of the file to return is passed as parameter.

## Parameters

| Name | Description |
|---|---|
| buffer | Space for the returned string. |
| bufferSize | Size of the buffer. |
| index | Index of the returned offline file. |

## Example

```c
long isActive;
char buffer[256];
long numFiles;
long i;

write("Offline source files:");
numFiles = getNumOfflineFiles();
for (i = 0; i < numFiles; ++i)
{
  getOfflineFileName(i, buffer, 256);
  write("%s", buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2: form 1 11.0: form 2 | 7.2: form 1 11.0: form 2 | 13.0 | — | 14 | 1.0: form 1 3.0: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
