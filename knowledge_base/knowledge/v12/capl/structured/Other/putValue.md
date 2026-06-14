# putValue

> Category: `Other` | Type: `function`

## Syntax

```c
void putValue(EnvVarName, int val); // form 1
```

## Description

Assigns the value val to the environment variable with identifier EnvVarName/name. Integers are assigned to discrete environment variables (form 1 and 6), floating point numbers are assigned to continuous environment variables (form 2 and 7). The contents of a character string is assigned to character string environment variables (form 3 and 8). For data byte environment variables (form 4, 5, 9 and 10) the bytes of the data buffer are copied into the environment variable.

## Return Values

—

## Example

```c
byte dataBuf[64];
...
// Assign the value 0 to environment variable Switch
putValue(Switch, 0);
// Assign the value 22.5 to environment variable Temperature
putValue(Temperature, 22.5);
// Assign the value Master to environment variable NodeName
putValue(NodeName, "Master");
// Copy 64 bytes of the data buffer into the environment variable DiagData
putValue(DiagData, dataBuf, 64);
...
```

## Availability

| Since Version |
|---|
