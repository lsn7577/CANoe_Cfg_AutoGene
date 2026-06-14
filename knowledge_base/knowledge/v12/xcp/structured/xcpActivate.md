# xcpActivate

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpActivate (char namespace[], char variable[]);
```

## Description

Activates an a2l parameter for upload and DAQ measurement.

Using system variables structs, the function must be used for the variable valid for the entire struct but not for single members.

## Return Values

0: OK

## Example

```c
on start
{
   if(0 == XcpActivate(sysvar::XCP::XcpSim::ampl))
   {
      write(„Parameter ampl activated for measurement“);
   }
}
```

## Availability

| Since Version |
|---|
