# coOnLssEvent

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnLssEvent( dword evType, dword param, dword param2 );
```

## Description

This function is called if the response of a LSS command was received. This can be triggered by one of the LSS functions. If during the execution an error occurs, the event function coOnError is called instead of these.

## Return Values

—

## Example

```c
void coOnLssEvent( dword evType, dword param, dword param2 ){
  write( "LSS event occurred 0x%x", evType );
}
```

## Availability

| Up to Version |
|---|
