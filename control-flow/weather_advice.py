user_weather_condition = input("What is the weather like today? (sunny, rainy, snowy): ").strip().lower()
if user_weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_weather_condition == "rainy":
          print("Don't forget your umbrella and a raincoat.")
elif user_weather_condition == "snowy":
       print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I dont have recommendations for this weather")