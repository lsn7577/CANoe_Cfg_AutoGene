# Iso11783AppErrorIndication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783AppErrorIndication( long ecuHandle, long errorClass, long errorNumber, long addCode );
```

## Description

Indicates that errors have occurred during a transfer or else during the initialization of ECUs (for example timeout during the transport protocol). If an Address Claiming procedure has failed, that will also be reported by means of this function.

## Return Values

—

## Example

```c
dword Iso11783AppErrorIndication( 
 LONG ecuHdl, LONG errClass, LONG errNum, LONG addCode )
{
  /* user code */
  return 0;
}
```

## Availability

| Since Version |
|---|
