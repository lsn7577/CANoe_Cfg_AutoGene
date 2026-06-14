# OnXcpEvent

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpEvent(char ecuQualifier[], byte data[], long dataSize);
```

## Description

This callback provides access to data that is sent from an XCP or CCP slave in an Event packet. The first data byte contains the type of the Event (named Code in the XCP specification).

## Return Values

—

## Availability

| Since Version |
|---|
