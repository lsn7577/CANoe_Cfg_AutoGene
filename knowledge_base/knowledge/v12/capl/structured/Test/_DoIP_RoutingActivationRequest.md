# _DoIP_RoutingActivationRequest

> Category: `Test` | Type: `function`

## Syntax

```c
long _DoIP_RoutingActivationRequest(dword sourceAddress, dword activationType, dword reserved, dword OEM, BYTE sendResponse[], BYTE responseCodeOut[]);
```

## Description

A request for routing activation was received in a vehicle simulation. It is possible to ignore, accept or deny the request, and to specify if a response message is sent.

## Example

```c
long _DoIP_RoutingActivationRequest(dword sourceAddress, dword activationType,dword reserved, dword OEM, BYTE sendResponse[], BYTE responseCodeOut[])
{
  write("_DoIP_RoutingActivationRequest(%04x, 0x%02x, reserved=%08x, OEM=%08x)"
  , sourceAddress, activationType, reserved, OEM);
  // sendResponse[0]    is always 1    (default: send response)
  // responseCodeOut[0] is always 0x10

  // Accept default or WWH-OBD
  if(activationType <= 0x01)
    return 0;  // continue with default behavior

  // Ignore a specific activation type, i.e. do not even send a response
  if(activationType == 0x99)
  {
    sendResponse[0] = 0;
    return 1;  // deny routing activation
  }

  // Accept a specific activation type only if reserved value is correct
  if(IsValidForActivationType( activationType, reserved))
    return 2;  // allow routing activation

  // All other activation types shall be denied
  responseCodeOut[0] = 0x06; // UnsupportedActivationType
  return 1; // deny routing activation
}
```

## Availability

| Since Version |
|---|
