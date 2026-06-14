# GNSSAppErrorIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSAppErrorIndication( long errNum, long errClass, long addInfo )
```

## Description

This function identifies errors that occurred during a transfer or else during the initialization of the node (for example timeout during the transport protocol). If an Address Claiming procedure has failed, that will also be reported by means of this function.

The error classes and error codes are described here.

## Return Values

—

## Example

```c
void GNSSAppErrorIndication( LONG errorClass, LONG errorCode, LONG addInfo )
{
  write( „Error code = %d“,errCode);
}
```

## Availability

| Since Version |
|---|
