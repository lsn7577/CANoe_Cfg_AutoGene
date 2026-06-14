# MCDStartDataAcq/ MCDStartDataAcqAsync

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long MCDStartDataAcq( char moduleName[], int taskId, int pollingRate, char parameters[])
```

## Description

Configure and start the data acquisition. After a data acquisition is started the configured parameters are transferred to CANoe with the specified polling rate. The values can be obtained with MCDGetCurrentValue.

Using MCDStartDataAcqAsync the data acquisition is started asynchronous. This means that the current measuring is not interrupted during the call of this function.

## Return Values

0

## Availability

| Up to Version |
|---|
