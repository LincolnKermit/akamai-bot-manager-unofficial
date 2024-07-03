| Name           | Value                                             | Description                                                                                       |
| :------------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| `s_vi`         | `?`                                               | **Required**. Akamai cookie, used to identify unique visitors, with an ID and timestamp           |
| `s_fid`        | `xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx`               | **Required**. This cookie name is associated with the analytics service provided by Adobe's Site Catalyst |
|                |                                                   | product suite, containing a randomly generated, unique id.                                          |
| `_abck`        | `too long to paste + can contains sensitive data` | **Required**. This cookie is used to know information about the computer and prove it is a real browser. |
| `s_sq`         | `uri_format`                                      | **Required**. This cookie is necessary to track the URL of the page the user was on during requests. |
| `bm_sv`        | `[\s\S]`                                          | **Required**. Cookie used by Akamai Bot Manager to differentiate between human-generated and bot-generated |
|                |                                                   | web requests.                                                                                     |
| `ak_bmsc`      | `?`                                               | Cookie used to optimize performance and improve user experience on Akamai websites. Not required |
|                |                                                   | for login but recommended not to delete.                                                           |
| `aic_authui_{customer_id}` | `aic_authui_{customer_id}`        | **Required**. Unique identifier for the authentication session, where `{customer_id}` is replaced with the |
|                | `aic_authui_e0a70b4f-1eef-4856-bcdb-f050fee66aae`  | specific customer ID. Either this or the corresponding `{customer_id}` cookie is required for    |
|                |                                                   | login; deleting both will result in login failure.                                                 |
| `{customer_id}` | `e0a70b4f-1eef-4856-bcdb-f050fee66aae`          | **Required**. Unique identifier for the authentication session, typically used with `aic_authui_{customer_id}`  |
|                |                                                   | to validate login sessions.                                                                       |
