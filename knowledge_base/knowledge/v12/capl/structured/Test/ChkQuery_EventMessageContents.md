# ChkQuery_EventMessageContents

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventMessageContents (dword CheckId, byte buffer[], dword bufferlen);
check.QueryEventMessageContents (byte buffer[], dword bufferlen);
```

## Description

Stores the data bytes of the message, for which the event has been sent, in the buffer and returns the number of stored data bytes (DLC).

## Return Values

< 0: Refers the query error codes

## Availability

| Since Version |
|---|
