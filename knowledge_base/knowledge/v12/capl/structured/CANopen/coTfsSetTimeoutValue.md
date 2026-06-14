# coTfsSetTimeoutValue

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetTimeoutValue( dword timeout );
```

## Description

This function sets the general time-out of all test functions, insofar as individual functions do not make a separate parameter available for this. The default value at measurement start is 2500 ms. If the value is set to 0, the function waits endlessly.

## Return Values

Error code

## Example

```c
coTfsSetTimeoutValue (300); // set time-out to 300 ms
```
