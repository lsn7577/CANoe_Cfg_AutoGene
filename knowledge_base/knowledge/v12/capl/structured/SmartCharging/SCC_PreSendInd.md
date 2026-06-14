# SCC_PreSendInd

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_PreSendInd ( byte SessionID[], dword MessageID, char ResponseCode[] )
```

## Description

The callback is called in active mode before a response message is sent. It enables checking the message’s response code and, if desired, overwriting it with another value. Additionally, overwriting the following parameters is supported:

## Return Values

—

## Availability

| Since Version |
|---|
