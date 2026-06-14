# Iso11783PDDSetParameter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetParameter( dword ecuHandle, char paramName[], float paramValue );
```

## Description

Changes an internal parameter of the PDD API.

## Example

```c
if (Iso11783PDDSetParameter( ecuHandle, "debug", 1 ) == 0) {
  write( "Debug mode activated" );
}
```

## Availability

| Since Version |
|---|
