
# Akamai Bot Manager Wiki

A great wiki to share and learn about Akamai Bot Manager for Devs.

## Structure


<img width="671" alt="image" src="https://github.com/LincolnKermit/akamai-bot-manager-unofficial/assets/104798220/9e5f2e8a-3786-44ca-8577-033378bce0ff">




## Usage/Examples

```python
import requests as s


headers = {"put some headers"}


# Initial requests to get appropriate cookie on the main page

request_get = s.get("https://google.com/" headers=headers)


# Final requests with the cookies


requests_post = s.post("https://google.com/login" headers=headers, cookie=request_get.cookie)

# Note that cookies may also be in the headers.
# Note also that cookie may contains date or time and can be rejected if the time doesn't match.


```





#### Cookie Wiki
| Name           | Value                                             | Required | Description                                                                                       |
| :------------- | :------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------ |
| `s_vi`         | `?`                                               | Yes      | Akamai cookie, used to identify unique visitors, with an ID and timestamp                         |
| `s_fid`        | `xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx`               | Yes      | This cookie name is associated with the analytics service provided by Adobe's Site Catalyst       |
|                |                                                   |          | product suite, containing a randomly generated, unique id.                                          |
| `_abck`        | `too long to paste + can contains sensitive data` | Yes      | This cookie is used to know information about the computer and prove it is a real browser.        |
| `s_sq`         | `uri_format`                                      | Yes      | This cookie is necessary to track the URL of the page the user was on during requests.            |
| `bm_sv`        | `[\s\S]`                                          | Yes      | Cookie used by Akamai Bot Manager to differentiate between human-generated and bot-generated      |
|                |                                                   |          | web requests.                                                                                     |
| `ak_bmsc`      | `?`                                               | No       | Cookie used to optimize performance and improve user experience on Akamai websites. Not required  |
|                |                                                   |          | for login but recommended not to delete.                                                           |
| `aic_authui_{customer_id}` | `aic_authui_{customer_id}`        | Yes      | Unique identifier for the authentication session, where `{customer_id}` is replaced with the     |
|                | `aic_authui_e0a70b4f-1eef-4856-bcdb-f050fee66aae`  |          | specific customer ID. Either this or the corresponding `{customer_id}` cookie is required for    |
|                |                                                   |          | login; deleting both will result in login failure.                                                 |
| `{customer_id}` | `e0a70b4f-1eef-4856-bcdb-f050fee66aae`          | Yes      | Unique identifier for the authentication session, typically used with `aic_authui_{customer_id}`  |
|                |                                                   |          | to validate login sessions.                                                                       |


#### Error Code Wiki

403 : Forbidden -> Cookie / Headers doesn't match or doesn't work.
428 : Same Requests repeated -> Crypto Challenge 



## Documentation

[Cookie Manager Documentation by Akamai](https://techdocs.akamai.com/identity-cloud/docs/hosted-login-cookies-and-local-storage-1)




## Related

Here are some related projects:

[Outdated Cookie Generator in Golang](https://github.com/i7solar/Akamai)

[Outdated Cookie Generator in TypeScript](https://github.com/zedd3v/abck)



## Disclaimer: Educational Information and Non-responsibility Notice

Please note that I am not responsible for the accuracy or reliability of the information provided about Akamai Technologies or any other topic discussed here. It's always recommended to verify information from reliable sources for any critical decisions or actions. Additionally, I am not liable for any illegal activities conducted based on the information provided here; this content is purely educational and should not be construed as legal advice or encouragement to engage in illegal activities.
## Authors

- [@LincolnKermit](https://www.github.com/LincolnKermit)

