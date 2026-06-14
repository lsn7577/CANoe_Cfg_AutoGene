# isOfflineFileActive

> Category: `Other` | Type: `function`

## Syntax

```c
long isOfflineFileActive(long index);
```

## Description

Returns whether events of an offline source file are currently replayed, i.e., the start of the source file has been reached but the end of the source file has not yet been reached.

## Parameters

| Name | Description |
|---|---|
| index | Index of the offline source file. |

## Example

```c
long isActive;
char buffer[256];
long numFiles;
long i;

numFiles = getNumOfflineFiles();
for (i = 0; i < numFiles; ++i)
{
  getOfflineFileName(i, buffer, 256);
  isActive = isOfflineFileActive(i);
  if (isActive)
  {
    write("Offline file %s is active", buffer);
  }
  else
  {
    write("Offline file %s is inactive", buffer);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
