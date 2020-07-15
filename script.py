def cost_ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  
  return (20 + (price_per_pound * weight))

print(cost_ground_shipping(8.4))

cost_premium_shipping = 125.00

def cost_drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 12.25
  
  return price_per_pound * weight

print(cost_drone_shipping(1.5))

def print_cheapest_method(weight):
  ground = cost_ground_shipping(weight)
  premium = cost_premium_shipping
  drone = cost_drone_shipping(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest available option is $%.2f with %s shipping."
  % (cost, method))

print_cheapest_method(4.8)
print_cheapest_method(41.5)