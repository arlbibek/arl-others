from datetime import datetime
import platform
import subprocess
import re


def get_host():
    """Return hostname of the device where the script is running."""
    return platform.node()


command_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()


profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search(
                "Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)


content = ""
for x in range(len(wifi_list)):
    content += f"{wifi_list[x]['ssid']:<25}=> {wifi_list[x]['password']}\n"

result = f"""# Know Wireless Networks on '{get_host()}' at {datetime.now()}

{'SSID':<25}   PASSWORD
{"-"*40}
{content}"""

# printing the result to the console
print(result)


# writing the result to a file
filename = "wifi_passwd.txt"
with open(filename, "wt") as pwd:
    pwd.write(result)

input(f"[ done ] password extracted, see '{filename}'")

# Referenced from [David Bombal](https: // youtu.be/SzYKzAHsdMg "Python WiFi")
