# J1587GetParameterByPID

> Category: `J1587` | Type: `function`

## Syntax

```c
byte J1587GetParameterByPID(J1587Message msg /*in*/, J1587Param param /*out*/, dword dbPID /*in*/)
```

## Description

Gets a J1587 parameter inside a J1708 message given a specific PID.

The function returns an error if a parameter with the specified dbPID is not found inside the J1708 message.

## Return Values

0 or error code

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  dword count, i;
  J1587Param param;

  if (J1587GetParameterByPID(this, param, 80) == 0)
  {
    write ("Parameter with PID 80 received.");
  }
}
```

## Availability

| Since Version |
|---|
