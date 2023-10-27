"""reduce and partials serve different purposes but can also work together."""
from functools import partial, partialmethod, reduce
from urllib.request import urlopen

def get_site_status(url):
    try:
        return urlopen(url).getcode()
    except:
        return

google_status = partial(get_site_status, "http://google.com")
facebook_status = partial(get_site_status, "http://facebook.com")
redhat_status = partial(get_site_status, 'http://www.redhat.com')
x_status = partial(get_site_status, 'http://www.twitter.com')

class VMManager:

    def toggle_power(self, to_state):
        if to_state == "on":
            print("Powering on VM")
        elif to_state == "off":
            print("Powering off VM")

    power_on = partialmethod(toggle_power, "on")
    power_off = partialmethod(toggle_power, "off")

# reduce
def multiply(num1, num2):
    print(f"multiplying {num1=} by {num2=}")
    return num1 * num2

factorial = partial(reduce, multiply)
