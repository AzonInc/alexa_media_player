import logging
from homeassistant.helpers.entity import Entity
from homeassistant.const import STATE_UNKNOWN
from .const import DOMAIN  # Adjust as needed

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Alexa ToDo List entity."""
    account = config_entry.data
    email = account.get("email")  # or use CONF_EMAIL if imported
    # Pass account-specific data from hass.data
    account_info = hass.data.get("DATA_ALEXAMEDIA", {}).get("accounts", {}).get(email, {})
    async_add_entities([AlexaTodoList(email, account_info)])

class AlexaTodoList(Entity):
    """Representation of an Alexa ToDo List entity."""

    def __init__(self, email, account_info):
        """Initialize the ToDo list entity."""
        self._email = email
        self._account_info = account_info
        self._name = f"Alexa ToDo List ({email})"
        self._state = STATE_UNKNOWN
        self._todos = []

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    @property
    def state(self):
        """Return the current state (for example, number of Todo items)."""
        return len(self._todos)

    @property
    def extra_state_attributes(self):
        """Return the attributes of the entity."""
        return {"todos": self._todos}

    async def async_update(self):
        """Fetch new state data for the entity.

        In a real-world scenario, use your Alexa API functions or process pending PUSH_TODO_CHANGE data.
        """
        # Placeholder: Replace with proper retrieval of the todo list for the account
        todos = await self._fetch_todos()
        self._todos = todos

    async def _fetch_todos(self):
        """Fetch the current todo list from Alexa.

        This is where you would integrate with Alexa API data that may be stored in the account_info.
        For example, if you've processed a PUSH_TODO_CHANGE event and stored the latest list in account_info.
        """
        # Replace with actual data retrieval logic.
        _LOGGER.debug("Fetching ToDo list for %s", self._email)
        return ["Buy milk", "Answer email"]  # example todos