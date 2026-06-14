# GetCANMessage

> Category: `Other` | Type: `function`

## Syntax

```c
long GetCANMessage(this, message * msg);
```

## Description

This function can only be called inside of an on PDU handler. The function will return in its second parameter the CAN (or CAN-FD) frame, the PDU was contained.

## Return Values

0: Data access successful.

## Example

```c
on PDU PDU_A
{
  message * aMsg_01;
  long result;
  result = GetCANMessage(this, aMsg_01); // PDU is assumed to be sent on CAN
  if (result == 0)
  {
    write("Received PDU 'PDU_A' in message with CAN ID %lu", aMsg_01.ID);
  }
  else
  {
    write("Error accessing PDU!");
  }
}
```

## Availability

| Since Version |
|---|
