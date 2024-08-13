from app.models.energy_model import EnergyUsage
from datetime import datetime, timedelta


def total_energy_consumption(device_id):
    usages = EnergyUsage.query.filter_by(device_id=device_id).all()
    total = sum([usage.usage_kwh for usage in usages])
    return total

def average_daily_consumption(device_id):
    usages = EnergyUsage.query.filter_by(device_id=device_id).all()
    if not usages:
        return 0
    start_date = min(usage.timestamp for usage in usages).date()
    end_date = max(usage.timestamp for usage in usages).date()
    days = (end_date - start_date).days + 1
    total = total_energy_consumption(device_id)
    return total / days if days > 0 else 0

def peak_usage_times(device_id):
    usages = EnergyUsage.query.filter_by(device_id=device_id).all()
    if not usages:
        return []
    
    usage_by_hour = [0] * 24
    for usage in usages:
        usage_by_hour[usage.timestamp.hour] += usage.usage_kwh

    peak_hours = [i for i, usage in enumerate(usage_by_hour)
                  if usage == max(usage_by_hour)]
    return peak_hours
