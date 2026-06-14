# J1587GetParameterCount

> Category: `J1587` | Type: `function`

## Syntax

```c
word J1587GetParameterCount(J1587Message msg /*in*/)
```

## Description

Gets the count of J1587 parameters inside a given J1708 message that can be used to further calls to J1587GetParameter().

## Return Values

number of parameters

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  write ("Number of parameters received: %d", J1587GetParameterCount(this));
}
```

## Availability

| Since Version |
|---|
