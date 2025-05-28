import json
from django.conf import settings
from pathlib import Path
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_KEY,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
)

def load_vehicles():
    dataset_path = Path(__file__).resolve().parent.parent / "data" / "vehicles.json"
    with open(dataset_path, "r") as f:
        return json.load(f)

def get_recommendation_from_gpt(user_query):
    vehicles = load_vehicles()

    # Optionally limit for token size
    top_vehicles = sorted(vehicles, key=lambda x: x['price'])[:20]

    # Format specs for GPT
    vehicle_text = "\n\n".join([
        f"Name: {v['name']}\n"
        f"Price: ${v['price']}, Year: {v['year']}, Condition: {v['condition']}\n"
        f"Type: {v['type']}, Fuel: {v['fuel_type']}\n"
        f"Mileage: {v['mileage']} km, Engine: {v['engine_size']}L\n"
        f"Seats: {v['seating_capacity']}, Safety: {v['safety_rating']}\n"
        f"Key Features: {v['features']}\n"
        for v in top_vehicles
    ])

    system_prompt = (
        "You are an expert assistant for a car dealership. A customer will describe what they need in natural language. "
        "Based on the full vehicle specs below, recommend the top matching vehicles, and explain why.\n\n"
        f"{vehicle_text}"
    )

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    return response.choices[0].message.content
