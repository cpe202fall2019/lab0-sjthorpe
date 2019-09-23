def weight_on_planets():
   earth_weight = float(input( "What do you weigh on earth? " ))
   mars_weight = 0.38 * earth_weight
   jupiter_weight = 2.34 * earth_weight
   print ( \n "On Mars you would weigh ", mars_weight, " pounds." \n "On Jupiter you would weigh ", jupiter_weight, " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()
