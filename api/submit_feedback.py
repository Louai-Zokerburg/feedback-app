import httpx


async def submit_feedback(name, email, feedback):
    url = "https://your-fake-api-endpoint.com/submit"
    payload = {"name": name, "email": email, "feedback": feedback}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            return response
        except httpx.RequestError as exc:
            print(f"An error occurred: {exc}")
            return None
