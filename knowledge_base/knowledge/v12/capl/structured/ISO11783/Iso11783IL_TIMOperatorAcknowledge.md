# Iso11783IL_TIMOperatorAcknowledge

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMOperatorAcknowledge( ); // form 1
```

## Description

This function performs an operator acknowledgement.

It sends a TIM_ServerStatus_Msg message with the Acknowledge indication for 3 times in a row

It changes the automation status of a TIM function to Automation Pending in case this TIM function is allowed for the operator acknowledgement.

## Return Values

0: Property has been set successfully

## Example

```c
Iso11783IL_ TIMOperatorAcknowledge ();
```

## Availability

| Since Version |
|---|
