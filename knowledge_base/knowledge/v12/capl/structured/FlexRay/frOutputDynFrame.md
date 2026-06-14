# frOutputDynFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
int ret = frOutputDynFrame( <frame var> );
```

## Description

This function updates the FlexRay Communication Controller's (CC) send buffer with the current data from the send object. This corresponds to a request to send.

Only frames in the dynamic segment can be sent using this function!

## Return Values

0: Ok, the request to send the frame is forwarded to the interface. This does not guarantee that the frame is really been sent. Refer to the FlexRay protocol rules.

## Availability

| Since Version |
|---|
