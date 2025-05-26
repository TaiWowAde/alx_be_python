def get_weather_advice(weather: str) -> str:
    weather = weather.lower()
    if weather == "sunny":
        return "Wear a t-shirt and sunglasses."
    elif weather == "rainy":
        return "Don't forget your umbrella and a raincoat."
    elif weather == "cold":
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

if __name__ == "__main__":
    user_input = input("What's the weather like today? (sunny/rainy/cold): ")
    print(get_weather_advice(user_input))
