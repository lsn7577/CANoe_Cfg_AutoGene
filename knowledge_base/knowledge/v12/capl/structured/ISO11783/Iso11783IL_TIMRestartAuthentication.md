# Iso11783IL_TIMRestartAuthentication

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMRestartAuthentication(dbNode server); // form 1
```

## Description

This function restarts the authentication process of a client/server communication.

The client restarts the authentication by setting the (Re)Start authentication status bit of the Auth_ClientAuthenticationStatusClient message.

This function only succeeds if the authentication process is currently active (especially if current state is Authentication error).

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
