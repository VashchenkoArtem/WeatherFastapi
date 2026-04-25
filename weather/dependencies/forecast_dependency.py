from fastapi import HTTPException

def validate_city(city_name: str | None = None):
    if not city_name:
        raise HTTPException(
            status_code=404,
            detail="City name does not found"
        )
    elif len(city_name.strip()) <= 2:
        raise HTTPException(
            status_code=400,
            detail="Invalid city name"
        )
    return city_name.strip()