def fertilizer_recommendation(N, P, K):
    if N < 50:
        return "Low Nitrogen: Apply Urea"
    elif P < 40:
        return "Low Phosphorus: Apply SSP"
    elif K < 40:
        return "Low Potassium: Apply MOP"
    return "Soil nutrients are balanced"
