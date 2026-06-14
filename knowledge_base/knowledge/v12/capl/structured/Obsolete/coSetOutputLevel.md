# coSetOutputLevel

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetOutputLevel( dword level, dword errCode[] );
```

## Description

The function sets the output level of the node layer.

It must be noted that this function may only be called if the node has been started.

## Return Values

—

## Example

```c
dword errCode[1];
coSetOutputLevel( 5, errCode );
```

## Availability

| Up to Version |
|---|
