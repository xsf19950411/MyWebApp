import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop,user='root', password='123456', database='mywebappdb')

    u = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop=asyncio.get_event_loop()

loop.run_until_complete(test(loop))
loop.close()