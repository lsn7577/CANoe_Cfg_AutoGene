# coSetSDOTimeout

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetSDOTimeout( dword time, dword errCode[] );
```

## Description

The function sets the time after which a SDO transmission is aborted if the communication partner does not response. The default value is 2000 ms and applies globally for all SDO transmission.

## Return Values

—

## Example

```c
dword errCode[1];

coSetSDOTimeout( 100, errCode );
if (errCode[0] == 0) {
  write( "SDO time-out set to 100ms" );
}
```

## Availability

| Up to Version |
|---|
