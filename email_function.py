import asyncio
from random import choice, randint


async def get_details(ipno,email: str) -> dict:
    """ This function takes in an email address and returns some details.

    Args:
        email (str): Stores the email address whose details are to be fetched.

    Returns:
        dict: The details of the email address.
    """
    boolean_list = [True, False]
    status = ["valid", "invalid", "unknown"]
    active = ["active", "inactive"]
    result = {
        "index":ipno,
        "domain": email.split("@")[1],
        "provider": email.split("@")[1].split(".")[0].title(),
        "is_valid": choice(boolean_list),
        "is_reachable": choice(boolean_list),
        "is_billable": choice(boolean_list),
        "mailbox_status": choice(active),
        "status": choice(status),
        "score": randint(0, 100),
    }
    await asyncio.sleep(randint(1, 10))
    return result


def main():
    print(asyncio.run(get_details("testing@derbatech.com")))


if __name__ == "__main__":
    main()

