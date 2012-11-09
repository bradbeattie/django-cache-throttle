from datetime import datetime
from hashlib import sha1
import json


class ActionThrottled(Exception):
    pass


# The cache entry _key_ can never have more points than _maximum_stamina_.
# When points are decremented via _decrement_, they're regenerated at the
# rate of _regenerate_per_hour_. With _regenerate_per_hour_ set to 900,
# that means one point per 4 seconds. If the stored number of points ever
# reaches the maximum_stamina, we don't bother storing it in the cache
# anymore and assume that any uncached entry has _maximum_stamina_ points.
def throttle(cache, key, decrement=1, maximum_stamina=10, regenerate_per_hour=10):

    # Convert the given key into something hashable
    key = "throttle:%s" % sha1(json.dumps(key)).hexdigest()

    # Determine the current stamina
    entry = cache.get(key)
    if (entry == None):
        current_stamina = maximum_stamina
    else:
        current_stamina = min(
            maximum_stamina,
            entry[0] + (datetime.now() - entry[1]).total_seconds() * (regenerate_per_hour / 3600.0)
        )

    # Decrement the current stamina and choke if it's too low
    current_stamina -= decrement
    if (current_stamina < 0):
        raise ActionThrottled(current_stamina + decrement)

    # Note the success by storing the newly decreased stamina
    cache.set(
        key,
        (current_stamina, datetime.now()),
        3600.0 * (maximum_stamina - current_stamina) / regenerate_per_hour
    )
    return current_stamina

