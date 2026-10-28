# Smart Irrigation System

# A smart irrigation system uses soil moisture, water availability and rain condition to decide following
# condition:

# a) Check when irrigation is not required

# b) Check whether to Switch ON water pump or not

# Assume following status of irrigation system:

# 1. 1. 1. 1. 1. soil_is_dry = True
# 2. water_available = True
# 3. rain_detected = False

soil_is_dry = True
water_available = True
rain_detected = False

if soil_is_dry and water_available and not rain_detected:
    print("Irrigation is required. Switch ON the water pump.")
else:
    print("Irrigation is not required.")

