# Iso11783IL_OPStoreVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPStoreVersion( char versionName[] ); // form 1
```

## Description

The function stores the current object pool on the Virtual Terminal. A Store Version command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPStoreVersion( 
 "POOL01A" );
```

## Availability

| Since Version |
|---|
