# Здесь представлен пример без контекста async with
import asyncio

from glQiwiApi import QiwiWrapper

# Создаем объект кошелька и обязательно передаем without_context = True,
# иначе будут проблемы с aiohttp.ClientSession
wallet = QiwiWrapper(
    api_access_token="token",
    phone_number="+number",
    secret_p2p="your secret p2p",
    without_context=True,
)


async def main():
    bill = await wallet.create_p2p_bill(amount=1)
    # new version
    new_status = await bill.paid
    # old version
    old_status = (await wallet.check_p2p_bill_status(bill.bill_id)) == "PAID"
    assert new_status == old_status


asyncio.run(main())
