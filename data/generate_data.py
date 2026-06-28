import numpy as np
import pandas as pd

np.random.seed(42)

roads = ["A6", "A9", "A93"]

weather_options = [
    "Clear",
    "Rain",
    "Fog",
    "Snow"
]

rows = []

for road in roads:

    for station in range(1,11):

        km = station * 15

        lanes = np.random.choice([2,3,4])

        for day in range(1,8):

            date = pd.Timestamp("2023-08-01") + pd.Timedelta(days=day)

            for hour in range(24):

                for minute in [0,5,10,15,20,25,30,35,40,45,50,55]:

                    timestamp = date + pd.Timedelta(
                        hours=hour,
                        minutes=minute
                    )

                    rush = hour in [7,8,9,16,17,18]

                    if rush:
                        flow = np.random.randint(1800,2400)
                        speed = np.random.randint(20,80)
                        occupancy = np.random.randint(60,100)
                    else:
                        flow = np.random.randint(500,1500)
                        speed = np.random.randint(80,130)
                        occupancy = np.random.randint(10,60)

                    truck = np.random.uniform(5,25)

                    weather = np.random.choice(
                        weather_options,
                        p=[0.65,0.2,0.1,0.05]
                    )

                    construction = np.random.choice(
                        [0,1],
                        p=[0.95,0.05]
                    )

                    accident = np.random.choice(
                        [0,1],
                        p=[0.98,0.02]
                    )

                    jam = (
                        (speed < 30 and occupancy > 80)
                        or construction
                        or accident
                    )

                    rows.append([
                        timestamp,
                        road,
                        f"{road}_Station_{station}",
                        km,
                        lanes,
                        flow,
                        speed,
                        occupancy,
                        truck,
                        weather,
                        construction,
                        accident,
                        int(jam)
                    ])

traffic = pd.DataFrame(rows, columns=[
    "Timestamp",
    "Road",
    "Station",
    "Kilometer",
    "Lanes",
    "Flow",
    "Speed",
    "Occupancy",
    "Truck_Percentage",
    "Weather",
    "Construction",
    "Accident",
    "Traffic_Jam"
])

traffic.to_csv(
    "simulated_realtime_traffic.csv",
    index=False
)

print(traffic.head())
print(traffic.shape)