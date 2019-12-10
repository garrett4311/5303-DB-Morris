### Barebones Refactor - Worst Flight Planner Step 2

The instructions for this assignment were to normalize the data from A04. I
decided that the ICAO and IATA columns were unnecessary for the Airports,
Airlines, and Planes tables. I also removed the Tz Database Timezone column was
not needed in the Airports table. The final thing I did was completely remove
the Routes table, as it was confusing and I wasn't sure how we would make much
use of it.
