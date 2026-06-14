# sysExec, sysExecCmd

> Category: `Other` | Type: `function`

## Syntax

```c
long sysExec(char cmd[], char params[]);
```

## Description

Executes an external command. Does not wait until the command has completed its execution.

sysExec must be given an executable; sysExecCmd calls cmd.EXE /K with the first parameter, which opens a command window where the command is executed as if it was entered directly.

## Return Values

1 if the command was successfully started, else 0.
Note
Note that no return value from the command itself is given because the call does not wait for the command to finish.

## Example

```c
char configDir[1024];
getAbsFilePath("", configDir, elcount(configDir)); 
sysExecCmd("dir", "/O:-D", configDir); // show files in configuration directory, newest files first
```

## Availability

| Since Version |
|---|
