# A664CloseProxyPort

> Category: `ADFX` | Type: `function`

## Syntax

```c
long a664CloseProxyPort (WORD channel, DWORD outMsgId)
```

## Description

Method to close a specific socket port, which was generated using a664InitProxyPort.

This call is only required, if an existing message-pair or UDP-port combination needs to be modified.

On measurement end all existing proxy-ports are closed automatically.

## Availability

| Since Version |
|---|
