# sysExec, sysExecCmd

> Category: `Other` | Type: `function`

## Syntax

```c
long sysExec(char cmd[], char params[]); // form 1
long sysExec(char cmd[], char params[], char directory[]); // form 2
long sysExecCmd(char cmd[], char params[]); // from 1
long sysExecCmd(char cmd[], char params[], char directory[]); // form 2
```

## Description

Executes an external command. Does not wait until the command has completed its execution.

sysExec must be given an executable; sysExecCmd calls cmd.EXE /K with the first parameter, which opens a command window where the command is executed as if it was entered directly.

## Parameters

| Name | Description |
|---|---|
| cmd | The command to be executed. Either the full absolute path or a path relative to the current working directory must be given or the command must be in the system path. |
| params | Parameters to the command. A parameter which contains spaces must be enclosed in " ". |
| directory (Form 2) | Working directory for the command. Either an absolute path or a path relative to the current working directory must be given. |

## Return Values

1 if the command was successfully started, else 0.

## Example

Example 1

If the working directory of CANoe is not the same as the directory of a called program, the path for this program must be given in the function.

Example 2

```c
sysExec("C:\\Program Files\\Beyond Compare 3\\BCompare.EXE", Commandline, "C:\\Program Files\\Beyond Compare 3");
char configDir[1024];
getAbsFilePath("", configDir, elcount(configDir)); 
sysExecCmd("dir", "/O:-D", configDir); // show files in configuration directory, newest files first
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP3 | 7.2 SP3 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
