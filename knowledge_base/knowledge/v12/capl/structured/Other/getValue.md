# getValue

> Category: `Other` | Type: `function`

## Syntax

```c
int getValue(EnvVarName); // form 1
```

## Description

Determines the value of the environment variable with identifier EnvVarName/name. The type of the return value is based on the type of environment variable (int for discrete (form 1), float for continuous environment variables (form 2 and 6)). For character string environment variables (form 3 and 7) and environment variables with data bytes (form 4, 5, 8 and 9) the active value is saved to a buffer which you identify in the function call.

## Return Values

Form 1 and 2
Active value of the environment variable.

## Example

```c
int val;
float fval;
char cBuf[25];
byte bBuf[64];
long copiedBytes;
...
// Assign to val the value of the environment variable Switch
val = getValue(Switch);
// Assign to fval the value of the environment variable Temperature
val = getValue(Temperature);
// Read the value of environment variable NodeName
copiedBytes = getValue(NodeName, cBuf);
// Read the value of environment variable DiagData
copiedBytes = getValue(DiagData, bBuf);
// Read the value of environment variable DiagData starting at position 32
copiedBytes = getValue(DiagData, bBuf, 32);
...
```

## Availability

| Since Version |
|---|
