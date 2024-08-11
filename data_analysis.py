from app.controllers.energy_controller import calculate_total_energy_consumed


def analyze_energy_usage(user_id):
    total_energy = calculate_total_energy_consumed(user_id)
    return {
        "user_id": user_id,
        "total_energy_consumed": total_energy
    }
