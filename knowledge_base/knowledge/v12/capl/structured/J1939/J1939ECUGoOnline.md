# J1939ECUGoOnline

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939ECUGoOnline( dword ecuHandle, dword newAddress );
```

## Description

After this function has been called, the logical ECU logs on onto the CAN bus. It must be called separately for each logical ECU.

If it is not possible to log on the first time with Address Claiming, or if the node is "rejected" with a higher priority Address Claiming by the bus at a later point in time, the corresponding error message must be evaluated in J1939AppErrorIndication(). If you want to make a network assignment over the network, the PG "CommandedAddress" can be sent to an ECU.

Use the Null Address (0xFE) to switch the ECU to offline mode. In that explicit case a "Cannot Claim" message ("Address Claim" PG from source address 0xFE) is sent once.

It is not possible to claim the broadcast address 0xFF.

## Return Values

0 on success or error code

## Example

```c
J1939ECUGoOnline(ecuHdl, 0x06);
```

## Availability

| Since Version |
|---|
