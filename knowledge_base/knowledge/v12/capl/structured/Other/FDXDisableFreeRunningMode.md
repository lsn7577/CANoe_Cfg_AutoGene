# FDXDisableFreeRunningMode

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXDisableFreeRunningMode(long fdxClientHandle, word groupID);
```

## Description

This function disables the Free Running mode for the specified FDX client. The behavior of the function corresponds to the reception of a FreeRunningCancel command via the CANoe FDX protocol.

You can find further information about the Free Running mode in the manual CANoe_FDX_Protocol_EN.pdf.

## Return Values

0: Successful function call

## Availability

| Since Version |
|---|
