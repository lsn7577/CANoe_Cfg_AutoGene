# Iso11783PDDSetLogTrigger

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetLogTrigger( dword ecuHandle, dword command, ulong ddi, ulong elNum, ulong value );
```

## Description

A measurement command can be executed with this function. It can be used in the callback function Iso11783PDDOnDefaultLogRequest to activate the default logging.

## Return Values

error code

## Example

```c
void Iso11783PDDOnDefaultLogRequest 
 ( dword ecuHandle )
{
 Iso11783PDDSetLogTrigger
 ( ecuHandle, 4, 0x0100, 0, 1000 );
 Iso11783PDDSetLogTrigger
 ( ecuHandle, 4, 0x0101, 0, 1000 );
}
```

## Availability

| Since Version |
|---|
