# GPIBGetError

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBGetError (void);
```

## Description

Returns the error variable. It is meaningful only when the ERR bit in the status word is set

## Return Values

Current error status

## Example

```c
// “40” is not a valid GPIB address
GPIBDevChangePrimAddr(devDescr, 40);
if ( ( 1 << 15) & GPIBGetStatus() )
{
   write("ERR bit set in status word");
   if ( 4 == GPIBGetError() )
   {
      write("error is EARG: Invalid argument to function call");
   }
}
```

## Availability

| Since Version |
|---|
