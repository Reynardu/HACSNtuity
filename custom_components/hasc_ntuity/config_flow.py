from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
import voluptuous as vol

DOMAIN = "hasc_ntuity"

class HascNtuityConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """User initiated setup."""
        if user_input is not None:
            # Hier können Sie die eingegebenen Daten überprüfen und speichern
            return self.async_create_entry(
                title="HASC Ntuity",  # Titel für die Konfiguration
                data=user_input
            )

        # Hier wird das Konfigurationsformular mit den benötigten Feldern angezeigt
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("site_id"): str,
                    vol.Required("bearer_token"): str,
                    vol.Required("username"): str,
                    vol.Required("password"): str,
                }
            ),
        )
