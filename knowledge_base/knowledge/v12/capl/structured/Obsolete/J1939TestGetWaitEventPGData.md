# J1939TestGetWaitEventPGData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword J1939TestGetWaitEventPGData( pg pgBuffer, dword pgBufferSize );
```

## Description

If a message event is the last event that triggers a wait instruction, the message content can be called up with this function.

## Example

```c
long lret;
pg EngineParameter engParam;

lret = J1939TestWaitForPG(10, 0xFF, 0xF123, 500 );
switch(lret) {
case 1:
  if (J1939TestGetWaitEventPGData(engParam, elcount(engParam) ) == 0) {
    gValue = engParam.engineSpeed;
  }
  break;
default:
  // error, timeout or constraint violation
  break;
}
```

## Availability

| Up to Version |
|---|
