# Iso11783OPExecuteMacro

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPExecuteMacro( dword ecuHandle, dword macroID );
```

## Description

The function executes a macro object. An Execute Macro command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPExecuteMacro( 
 handle, 1200 );
```

## Availability

| Since Version |
|---|
