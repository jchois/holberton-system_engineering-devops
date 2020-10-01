from datadog import initialize, api

options = {
    'api_key': '7e2c85a71d72c332cb6b80e12fbc723c',
    'app_key': '1df351dc5a4a39693712413f425eea8667511ec7'
}

initialize(**options)

print(api.Dashboard.get_all())
