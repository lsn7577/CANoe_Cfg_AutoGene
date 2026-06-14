# Iso11783OPESC

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPESC( dword ecuHandle );
```

## Description

The function aborts user input on the Virtual Terminal. A ESC command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPESC( 
 ecuHandle );
```

## Availability

| Since Version |
|---|
