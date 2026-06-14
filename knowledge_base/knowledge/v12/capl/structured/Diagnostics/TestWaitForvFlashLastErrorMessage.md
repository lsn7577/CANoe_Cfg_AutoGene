# TestWaitForvFlashLastErrorMessage

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long TestWaitForvFlashLastErrorMessage(char errorText[], dword maxLength);
```

## Description

Waits until the last detailed error message is retrieved from vFlash. If a message is received, it is copied into the given buffer.

## Return Values

1: Success

## Availability

| Since Version |
|---|
