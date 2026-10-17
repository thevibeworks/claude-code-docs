# Service map

| Service | Team | Database | Other dependencies |
|---|---|---|---|
| checkout | payments | db-primary | stripe-api |
| cart | storefront | db-primary | none |
| inventory | supply | db-inventory | redis cache in front of SKU lookups |
| auth | identity | none | idp.internal |

checkout and cart share db-primary. When one of them hammers it, the other one suffers. A page on cart with no cart deploy is very often checkout's problem, and the other way round. Check `db-primary` metrics before blaming the paged service.

inventory has its own database. Nothing else reads db-inventory.
