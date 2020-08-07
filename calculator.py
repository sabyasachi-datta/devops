# Extracting trips data
def get_trips(START_DATE, END_DATE, SESSION):
    import pandas as pd
    import time
    import os
    from query import get_trips_query
    from connection import get_csv_s3
    timer_a = time.time()
    get_csv_s3(get_trips_query(START_DATE, END_DATE, SESSION))
    trips_df = pd.read_csv('file.csv')
    os.remove('file.csv')
    timer_b = time.time() #timer_end
    print(time.strftime('%H:%M:%S', time.localtime()), 
          (': Retrieved trips Details ' + 'in :{:0.3f} seconds').format(timer_b - timer_a))
    return trips_df

# Extracting trip history data
def get_trip_history(START_DATE, END_DATE, SESSION):
    import pandas as pd
    import time
    import os
    from query import get_trip_history_query
    from connection import get_csv_s3
    timer_a = time.time()
    get_csv_s3(get_trip_history_query(START_DATE, END_DATE, SESSION))
    trip_history_df = pd.read_csv('file.csv')
    os.remove('file.csv')
    timer_b = time.time() #timer_end
    print(time.strftime('%H:%M:%S', time.localtime()), 
          (': Retrieved trip history Details ' + 'in :{:0.3f} seconds').format(timer_b - timer_a))
    return trip_history_df