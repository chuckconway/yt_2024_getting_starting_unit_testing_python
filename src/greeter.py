import asyncio


class Greeter:
    # Simulate an asynchronous method that fetches a greeting prefix
    async def get_greeting_prefix(self):
        await asyncio.sleep(0.1)  # Simulate some async operation
        return "Hello"

    # Main async method that uses the get_greeting_prefix method
    async def greet(self, name):
        prefix = await self.get_greeting_prefix()
        return f"{prefix}, {name}!"