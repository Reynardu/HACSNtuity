DOMAIN = "hasc_ntuity"

def setup(hass, config):
    hass.states.set("hasc_ntuity.world", "Rey")

    return True