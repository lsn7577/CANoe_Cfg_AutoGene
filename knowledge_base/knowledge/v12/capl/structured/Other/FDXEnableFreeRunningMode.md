# FDXEnableFreeRunningMode

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXEnableFreeRunningMode(long fdxClientHandle, word groupID, word flags, dword cycleTime, dowrd firstDuration);
```

## Description

This function activates the Free Running mode for the specified FDX client. The behavior of the function corresponds to the reception of a FreeRunningRequest command via the CANoe FDX protocol.

You can find further information about the Free Running mode in the manual CANoe_FDX_Protocol_EN.pdf.

## Return Values

0: Successful function call

## Availability

| Since Version |
|---|
