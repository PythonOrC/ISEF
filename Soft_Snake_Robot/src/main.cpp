#include <Arduino.h>

#include "Masterborad.hpp"
#include "Slaveborad.hpp"

void setup()
{
}

void loop()
{
#ifdef MASTER
  masterfunction();
#endif

#ifdef SLAVE
  slavefunction();
#endif // SL
}
