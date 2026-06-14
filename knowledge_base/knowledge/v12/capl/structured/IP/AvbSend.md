# AvbSend

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbSend(dword talkerHandle, int buffer[], dword& length, char onSendCallback[]); // form 1
```

## Description

The function sends the data passed in the buffer. If the send operation completes immediately the function returns the number of sent elements in the length parameter and the passed CAPL callback OnAvbSend will not be called.

If the send operation does not complete immediately the operation is performed asynchronously and the function will return 460609.

In this case the CAPL callback OnAvbSend will be called on completion (successful or not).

No data should be written to the buffer until the send operation is complete to avoid corruption of the sent data.

## Return Values

0: The function completed successfully.

## Availability

| Since Version |
|---|
