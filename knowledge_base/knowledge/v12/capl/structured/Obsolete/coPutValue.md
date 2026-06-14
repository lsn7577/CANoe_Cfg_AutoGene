# coPutValue

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coPutValue( char envVar[], long value, dword errCode[] );
```

## Description

The function sets the value of an environment variable of the type integer.

In contrast to the putValue function of CANoe, with this function the name for runtime can be specified via a string and it does not already have to be known at translation time. This means, for example, it can be combined at runtime with the help of string functions.

## Return Values

—

## Example

```c
dword errCode[1];

coPutValue("envVarStart", 1, errCode);
if (errCode[0] == 0) {
  write( "Value of the environment variable successfully set" );
}
```

## Availability

| Up to Version |
|---|
