# vtsSetOutputRange

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetOutputRange (char Target[], eVTSOutputRange Range);
```

## Description

Sets the range that is used for analog output on output channels of VT2816 modules.

## Return Values

0: Successful call

## Example

```c
vtsSetOutputRange ("VTS::TempSensor”, eVTSOutputRangePlusMinus10V);
```

## Availability

| Since Version |
|---|
