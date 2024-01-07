from homeassistant.helpers.entity import Entity
import requests

DOMAIN = "hasc_ntuity"


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([HascNtuitySensor()])


class HascNtuitySensor(Entity):
    def __init__(self):
        self._production = None
        self._consumption = None
        self._imported = None
        self._exported = None
        self._charged = None
        self._discharged = None
        self._co2_savings = None
        self._profit = None
        self._autarky = None

    @property
    def name(self):
        return "HASC Ntuity Sensor"

    @property
    def state_attributes(self):
        return {
            "production": self._production,
            "consumption": self._consumption,
            "imported": self._imported,
            "exported": self._exported,
            "charged": self._charged,
            "discharged": self._discharged,
            "co2_savings": self._co2_savings,
            "profit": self._profit,
            "autarky": self._autarky,
        }

    def update(self):
        # Hier können Sie die Logik für das Aktualisieren der Werte von Ihrer Datenquelle implementieren
        # Beispiel: Rufen Sie die Daten von Ihrer API ab
        api_url = "https://navi.ntuity.io/api/v1/sites/" + self.id + "/production_and_consumption"
        params = {
            'from': '2021-01-01',
            'to': '2099-01-31',
            'totals_only': 'true'
        }
        headers = {
            "authorization": "Bearer " + self.login_bearer
        }
        try:
            response = requests.get(api_url)
            data = response.json()

            # Setzen Sie die Werte basierend auf der API-Antwort
            self._production = data.get("production", None)
            self._consumption = data.get("consumption", None)
            self._imported = data.get("imported", None)
            self._exported = data.get("exported", None)
            self._charged = data.get("charged", None)
            self._discharged = data.get("discharged", None)
            self._co2_savings = data.get("co2_savings", None)
            self._profit = data.get("profit", None)
            self._autarky = data.get("autarky", None)

        except Exception as e:
            # Behandeln Sie Fehler bei der API-Anfrage
            self._production = None
            self._consumption = None
            self._imported = None
            self._exported = None
            self._charged = None
            self._discharged = None
            self._co2_savings = None
            self._profit = None
            self._autarky = None

        self.schedule_update_ha_state()
