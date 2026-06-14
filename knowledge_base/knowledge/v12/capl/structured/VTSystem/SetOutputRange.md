# SetOutputRange

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SetOutputRange (eVTSOutputRange Range);
```

## Description

Sets the range that is used for analog output on output channels of VT2816 modules.

## Return Values

0: Successful call

## Example

```c
sysvar::VTS::TempSensor.SetOutputRange (eVTSOutputRangePlusMinus10V);
```

## Availability

| Since Version |
|---|
