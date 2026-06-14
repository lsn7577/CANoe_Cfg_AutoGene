# OnXcpError

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpError (char ecuQualifier[], byte xcpCmd, byte xcpErrorCode);
```

## Description

Whenever the XCP slaves answers with a negative response (i.e. not 0xFF) the OnXCPError callback function is called.

## Return Values

—

## Availability

| Since Version |
|---|
