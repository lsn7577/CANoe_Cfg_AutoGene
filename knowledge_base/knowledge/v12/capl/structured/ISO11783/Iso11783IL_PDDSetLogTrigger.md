# Iso11783IL_PDDSetLogTrigger

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetLogTrigger( dword command, ulong ddi, ulong elNum, ulong value ); // form 1
```

## Description

A measurement command can be executed with this function. It can be used in the callback function Iso11783IL_PDDOnDefaultLogRequest to activate the default logging.

## Example

```c
void Iso11783IL_PDDOnDefaultLogRequest ( )
{
 Iso11783IL_PDDSetLogTrigger( 4, 0x0100, 0, 1000 );
 Iso11783IL_PDDSetLogTrigger( 4, 0x0101, 0, 1000 );
}
```

## Availability

| Since Version |
|---|
