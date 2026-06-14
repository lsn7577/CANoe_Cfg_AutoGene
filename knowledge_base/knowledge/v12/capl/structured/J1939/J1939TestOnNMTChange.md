# J1939TestOnNMTChange

> Category: `J1939` | Type: `function`

## Syntax

```c
void J1939TestOnNMTChange( long ecuHandle, long reason );
```

## Description

The function can be implemented in your CAPL program. The J1939 Test Service Library calls this function, if the NMT table changes. The CAPL program can react on this changes.

## Return Values

—

## Example

```c
void J1939TestOnNMTChange( LONG ecuHandle, LONG reason ) {

  char dn[8];
  int address;

  J1939TestNmtQueryDeviceName( ecuHandle, dn );
  address = J1939TestNMTQueryAddress( ecuHandle );

  switch(reason) {
  case 1: // Begin claiming
    break;
  case 2: // Claiming completed successful (250ms after begin)
    break;
  case 3: // Lost address
    break;
  }
}
```

## Availability

| Since Version |
|---|
