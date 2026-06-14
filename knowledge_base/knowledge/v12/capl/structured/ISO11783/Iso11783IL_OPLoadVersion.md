# Iso11783IL_OPLoadVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLoadVersion( char versionName[] ); // form 1
```

## Description

The function loads an object pool, which is stored on the Virtual Terminal. A Load Version command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPLoadVersion( 
"POOL01A" );
```

## Availability

| Since Version |
|---|
