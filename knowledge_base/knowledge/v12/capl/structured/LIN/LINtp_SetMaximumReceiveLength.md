# LINtp_SetMaximumReceiveLength

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_SetMaximumReceiveLength(dword maxRecLen);
```

## Description

Sets maximum number of bytes node can receive. If more data is indicated in a FirstFrame and FlowControl frames have been activated, an overflow FlowControl frame is sent.

## Return Values

—

## Availability

| Since Version |
|---|
