# VTIL_SetSignal

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetSignal( dbSignal signal, double value );
```

## Description

Sets the signal to the specified physical value. The message of the signal is sent according the configured send type.

## Return Values

0: Function has been executed successfully

## Example

```c
void SendLanguageCommand_English()
{
  VTIL_SetSignal( LC_VT::LanguageCodeCmd, 0x6E65 );
}
```

## Availability

| Since Version |
|---|
