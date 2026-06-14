# coOnRPDOMissing

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnRPDOMissing( dword pdoNumber );
```

## Description

The function is called if an event timer of a RPDO is activated and the PDO is not received in the defined time.

## Return Values

—

## Example

```c
void coOnRPDOMissing(dword pdoNumber){
  write( "Receive PDO %d is missing", pdoNumber);
}
```

## Availability

| Up to Version |
|---|
