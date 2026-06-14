# GNSSAppAddrClaimed

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSAppAddrClaimed();
```

## Description

Identifies an Address Claiming procedure that was performed successfully. In this manner the control device is able to communicate on the CAN bus. If the Address Claiming cannot be successfully performed, the GNSSAppErrorIndication function is called with the corresponding error code.

## Return Values

—

## Example

```c
void GNSSAppAddrClaimed()
{
  write( "Address Claiming was successful" );
}
```

## Availability

| Since Version |
|---|
