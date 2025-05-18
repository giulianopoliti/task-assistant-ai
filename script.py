import json

# Load files
with open("flows.json", "r", encoding="utf-8") as f:
    flows = json.load(f)

with open("placeholders.json", "r", encoding="utf-8") as f:
    placeholders = json.load(f)

# --- Task 2: Fix quotes in line 10
for flow in flows:
    if "routing" in flow and "conditional" in flow["routing"]:
        flow["routing"]["conditional"] = flow["routing"]["conditional"].replace("“", "\"").replace("”", "\"")

# --- Task 3: Update hours
placeholders["general_context"] = placeholders["general_context"].replace(
    "Monday to saturday 9:00 to 18:00 hrs.",
    "Monday to Friday 9:00 to 18:00 hrs, Saturday 9:00 to 13:00 hrs."
)

# --- Task 4: Add new flow
flows.append({
    "name": "administracion",
    "routing": {
        "conditional": "You're an expert on conversation analysis. Your mission is to detect if the client is asking about administration. Respond \"Administración\" if true, otherwise respond \"UNKNOWN\".",
        "route": [
            {
                "response": "UNKNOWN",
                "generate_answer_template": {
                    "template": "You are {assistant_name}, from {company_name},\n\n{company_description}.\n\nYour mission is: Ask if the user needs help with sales or other area.",
                    "mission": "hola! mi nombre es {assistant_name} 😊 ¿en qué puedo ayudarte hoy?"
                }
            },
            {
                "response": "Administración",
                "next_flow": "administracion_pedir_nombre"
            }
        ]
    }
})
flows.append({
    "name": "administracion_pedir_nombre",
    "routing": {
        "conditional": "Check if the customer has provided their full name. Reply TRUE if they gave full name (including last name), else FALSE.",
        "route": [
            {
                "response": "FALSE",
                "generate_answer_template": {
                    "template": "You are {assistant_name}, from {company_name},\n\nYour mission is: Ask for the user's full name.",
                    "mission": "me compartís tu nombre completo por favor?"
                }
            },
            {
                "response": "TRUE",
                "next_flow": "transfer_administracion"
            }
        ]
    }
})
flows.append({
    "name": "transfer_administracion",
    "forward_to": {
        "contact_round": "Administración"
    },
    "generate_answer": "te voy a poner en contacto con el equipo de administración. podés comunicarte con ellos directamente en wa.me/{{forward_to.contact.channel_external_id}}. gracias por tu tiempo!"
})

# --- Save files again
with open("flows_updated.json", "w", encoding="utf-8") as f:
    json.dump(flows, f, indent=2, ensure_ascii=False)

with open("placeholders_updated.json", "w", encoding="utf-8") as f:
    json.dump(placeholders, f, indent=2, ensure_ascii=False)
