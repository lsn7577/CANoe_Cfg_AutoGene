# coGetValue

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long coGetValue( char envVar[], dword errCode[] );
```

## Description

The function returns the current value of an environment variable of the type integer.

In contrast to the getValue function of CANoe, with this function the name for runtime can be specified via a string and it does not already have to be known at translation time. This means, for example, it can be combined at runtime with the help of string functions.

## Return Values

Value of the environment variable

## Example

```c
dword errCode[1];
long returnValue ;

returnValue = coGetValue("envVarStart", errCode);
if (errCode[0] == 0) {
  write( "Value of the environment variable is: %d", returnValue );
}
```

## Availability

| Up to Version |
|---|
